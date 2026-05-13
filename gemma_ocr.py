import os
import argparse
import concurrent.futures
from pathlib import Path
from google import genai
from google.genai import types

# Try to load environment variables from .env file for project-specific config
try:
    from dotenv import load_dotenv
    load_dotenv(override=True)
except ImportError:
    pass

def process_single_pdf(file_path, client, model_id, output_dir, output_format, overwrite=False):
    """Worker function to process a single PDF file."""
    ocr_file = output_dir / f"{file_path.stem}.{output_format}"
    
    if ocr_file.exists() and not overwrite:
        print(f"  Skipping {file_path.name}: Output already exists.")
        return True

    print(f"\nProcessing: {file_path.name}")
    try:
        # Upload the file to the Gemini API
        print(f"  Uploading {file_path.name}...")
        uploaded_file = client.files.upload(file=file_path)
        
        # Construct the prompt for OCR only
        prompt = """
        Extract all text from the provided PDF image accurately.
        Capture all names, dates, handwritten notes, and tabular data without summarization or commentary.
        """

        print(f"  Generating content for {file_path.name}...")
        response = client.models.generate_content(
            model=model_id,
            contents=[uploaded_file, prompt],
            config=types.GenerateContentConfig(
                system_instruction="You are a high-accuracy OCR assistant.",
            )
        )
        
        full_text = response.text.strip()

        # Save OCR result
        with open(ocr_file, "w", encoding="utf-8") as f:
            f.write(full_text)
        print(f"  Success! OCR saved: {file_path.name}")
        return True
    except Exception as e:
        print(f"  Error processing {file_path.name}: {e}")
        return False

def extract_pdf_text(input_folder, output_folder, output_format="txt", max_workers=5, overwrite=False):
    """
    Processes PDF files from a folder in parallel.
    """
    print(f"--- Starting Parallel PDF Text Extraction ({output_format}) ---")
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
    output_dir = Path(output_folder)
    output_dir.mkdir(parents=True, exist_ok=True)

    input_path = Path(input_folder)
    pdf_files = sorted(list(input_path.glob("*.pdf")))

    if not pdf_files:
        print(f"No PDF files found in {input_folder}")
        return

    print(f"Found {len(pdf_files)} PDF files. Starting parallel execution...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Pass the client and other args to the worker function
        futures = [
            executor.submit(process_single_pdf, pdf, client, model_id, output_dir, output_format, overwrite) 
            for pdf in pdf_files
        ]
        
        results = []
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    success_count = sum(1 for r in results if r)
    print(f"\n--- Extraction Complete ---")
    print(f"Successfully processed {success_count} out of {len(pdf_files)} files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text from PDFs using Gemma in parallel.")
    parser.add_argument("-i", "--input", default="examples", help="Input directory containing PDF files")
    parser.add_argument("-o", "--output", default="ocr_outputs/gemma", help="Output directory for OCR text")
    parser.add_argument("-f", "--format", choices=["txt", "jsonl", "md"], default="txt", help="OCR output format (default: txt)")
    parser.add_argument("-w", "--workers", type=int, default=5, help="Number of parallel workers (default: 5)")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing output files (default: False)")

    args = parser.parse_args()
    
    extract_pdf_text(args.input, args.output, output_format=args.format, max_workers=args.workers, overwrite=args.overwrite)
