import os
import csv
import json
import argparse
import concurrent.futures
from pathlib import Path
from google import genai

# Try to load environment variables from .env file for project-specific config
try:
    from dotenv import load_dotenv
    load_dotenv(override=True)
except ImportError:
    pass

def process_single_file(file_path, client, model_id, output_dir, overwrite=False):
    """Worker function to process a single markdown file for NER."""
    output_csv = output_dir / f"{file_path.stem}.csv"
    
    if output_csv.exists() and not overwrite:
        print(f"  Skipping {file_path.name}: Output already exists.")
        return True

    print(f"\nProcessing: {file_path.name}")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        prompt = f"""
        Identify all unique individuals (person names) mentioned in the text below. 
        
        Text:
        {text}
        
        Return the results as a JSON list of objects, each with a 'name' key.
        Example: [ {{"name": "John Doe"}}, ... ]
        """

        response = client.models.generate_content(
            model=model_id,
            contents=prompt,
            config={
                "response_mime_type": "application/json"
            }
        )
        
        # Parse the JSON response
        results = json.loads(response.text)
        
        if not results:
            print(f"  No person entities detected in {file_path.name}.")
            return True

        # Extract names and deduplicate
        unique_names = sorted(list(set([entry.get('name', 'Unknown') for entry in results])))

        # Save to CSV
        with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["PERSON NAME"])
            for name in unique_names:
                writer.writerow([name])
        
        print(f"  Success! Results saved: {file_path.name}")
        return True

    except Exception as e:
        print(f"  Error processing {file_path.name}: {e}")
        return False

def run_gemma_ner(input_path, max_workers=5, overwrite=False):
    print(f"--- Starting Parallel Gemma 4 NER ---")
    print(f"--- Max Workers: {max_workers} ---")
    print(f"--- Overwrite Existing: {overwrite} ---")
    
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

    print(f"Found {len(files)} files. Starting parallel execution...")

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

    args = parser.parse_args()
    
    run_gemma_ner(args.input, max_workers=args.workers, overwrite=args.overwrite)

# Example usage: 
#* python ner_tests/gemma_test.py -w 10 for skip existing files and run 5 concurrent workers (Skips existing)
#  * python ner_tests/gemma_test.py --overwrite (Re-runs everything)
#  * python ner_tests/gemma_test.py -i some_other_folder/ (Runs on a specific path) 