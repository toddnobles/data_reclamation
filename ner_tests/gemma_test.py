import os
import csv
import json
import argparse
import concurrent.futures
import time
import re
from pathlib import Path
from google import genai
from google.genai import errors

# Try to load environment variables from .env file for project-specific config
try:
    from dotenv import load_dotenv
    load_dotenv(override=True)
except ImportError:
    pass

def chunk_text(text, max_chars=8000, overlap=500):
    """Splits text into overlapping chunks at paragraph boundaries."""
    if len(text) <= max_chars:
        return [text]

    chunks = []
    start = 0
    while start < len(text):
        end = start + max_chars
        if end >= len(text):
            chunks.append(text[start:])
            break
        
        # Try to find a paragraph break (\n\n) near the target end
        last_break = text.rfind("\n\n", start, end)
        if last_break != -1 and last_break > start:
            end = last_break
        
        chunks.append(text[start:end])
        start = end - overlap # Move back a bit for overlap
        
    return chunks

def clean_markdown(text):
    """Converts HTML table tags to a simpler Markdown-like format to save tokens."""
    # 1. Remove newlines and extra spaces between tags to make it one long string
    text = re.sub(r'>\s+<', '><', text)
    # 2. Replace </tr> with a newline
    text = re.sub(r'</tr>', '\n', text)
    # 3. Replace <td> and <th> with a pipe |
    text = re.sub(r'<(?:td|th)>', ' | ', text)
    # 4. Strip all other remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # 5. Clean up multiple spaces and empty lines
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text.strip()

def process_single_file(file_path, client, model_id, output_dir, overwrite=False):
    """Worker function to process a single markdown file for NER with chunking and retry logic."""
    output_csv = output_dir / f"{file_path.stem}.csv"

    if output_csv.exists() and not overwrite:
        print(f"  Skipping {file_path.name}: Output already exists.")
        return True

    print(f"\nProcessing: {file_path.name}")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            full_text = f.read()

        # Clean the text to convert HTML tables to Markdown and save tokens
        full_text = clean_markdown(full_text)

        # Split into chunks to handle quota and context limits
        text_chunks = chunk_text(full_text)
        all_extracted_names = set()

        for i, chunk in enumerate(text_chunks):
            if len(text_chunks) > 1:
                print(f"    Processing chunk {i+1}/{len(text_chunks)} for {file_path.name}...")

            prompt = f"""
            Identify all unique individuals (person names) mentioned in the text below. 

            Text:
            {chunk}

            Return the results as a JSON list of objects, each with a 'name' key.
            Example: [ {{"name": "John Doe"}}, ... ]
            """

            max_retries = 5
            retry_count = 0
            chunk_success = False
            
            while retry_count < max_retries:
                try:
                    response = client.models.generate_content(
                        model=model_id,
                        contents=prompt,
                        config={
                            "response_mime_type": "application/json"
                        }
                    )

                    # Parse the JSON response
                    results = json.loads(response.text)
                    if results:
                        for entry in results:
                            name = entry.get('name')
                            if name and name.lower() != "unknown":
                                all_extracted_names.add(name)
                    
                    chunk_success = True
                    break

                except errors.ClientError as e:
                    if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                        retry_count += 1
                        wait_time = 35 # Default fallback
                        match = re.search(r"retry in ([\d\.]+)s", str(e))
                        if match:
                            wait_time = float(match.group(1)) + 1
                        
                        print(f"      Rate limit hit. Retrying in {wait_time}s... (Attempt {retry_count}/{max_retries})")
                        time.sleep(wait_time)
                    else:
                        print(f"      API Error: {e}")
                        break
                except Exception as e:
                    print(f"      Unexpected error: {e}")
                    break
            
            if not chunk_success:
                print(f"    Failed to process chunk {i+1} of {file_path.name}")

        # Save all unique names from all chunks to CSV
        if not all_extracted_names:
            print(f"  No person entities detected in {file_path.name}.")
        
        unique_names = sorted(list(all_extracted_names))
        with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["PERSON NAME"])
            for name in unique_names:
                writer.writerow([name])

        print(f"  Success! Results saved: {output_csv.name}")
        return True

    except Exception as e:
        print(f"  Fatal error processing {file_path.name}: {e}")
        return False

def run_gemma_ner(input_path, max_workers=5, overwrite=False, gt_filter_dir=None):
    print(f"--- Starting Parallel Gemma 4 NER ---")
    print(f"--- Max Workers: {max_workers} ---")
    print(f"--- Overwrite Existing: {overwrite} ---")
    if gt_filter_dir:
        print(f"--- Filtering by GT in: {gt_filter_dir} ---")

    # Load API Key (will be loaded from .env if present)
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not set.")
        print("Please set it in your environment or a .env file.")
        return

    client = genai.Client(api_key=api_key)
    model_id = "gemma-4-31b-it"

    # Ensure output directory exists
    output_dir = Path("ner_tests/outputs/gemma_test")
    output_dir.mkdir(parents=True, exist_ok=True)

    path = Path(input_path)
    files = [path] if path.is_file() else sorted(list(path.glob("*.md")))

    if not files:
        print(f"No files found in {input_path}")
        return

    # Apply GT filter if requested
    if gt_filter_dir:
        gt_path = Path(gt_filter_dir)
        gt_stems = {f.stem for f in gt_path.glob("*.csv")}
        files = [f for f in files if f.stem in gt_stems]
        print(f"Filtered down to {len(files)} files with matching Ground Truth.")

    if not files:
        print("No files remaining after filtering.")
        return

    print(f"Processing {len(files)} files. Starting parallel execution...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(process_single_file, f, client, model_id, output_dir, overwrite) 
            for f in files
        ]

        results = []
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    success_count = sum(1 for r in results if r)
    print(f"\n--- NER Complete ---")
    print(f"Successfully processed {success_count} out of {len(files)} files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run NER on markdown files using Gemma 4 in parallel.")
    parser.add_argument("-i", "--input", default="ocr_outputs/hyak_outputs", help="Input file or directory (default: ocr_outputs/hyak_outputs)")
    parser.add_argument("-w", "--workers", type=int, default=5, help="Number of parallel workers (default: 5)")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing output files (default: False)")
    parser.add_argument("--filter-gt", help="Directory of Ground Truth CSVs to filter input files by")

    args = parser.parse_args()

    run_gemma_ner(args.input, max_workers=args.workers, overwrite=args.overwrite, gt_filter_dir=args.filter_gt)
