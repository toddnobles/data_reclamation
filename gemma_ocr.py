import os
import argparse
import concurrent.futures
import tempfile
from pathlib import Path
from google import genai
from google.genai import types
from pypdf import PdfReader, PdfWriter

# Try to load environment variables from .env file for project-specific config
try:
    from dotenv import load_dotenv
    load_dotenv(override=True)
except ImportError:
    pass

def generate_ocr_for_file(client, model_id, uploaded_file):
    """Helper to call Gemini API for a given uploaded file."""
    prompt = """
    Extract all text from the provided PDF image accurately.
    Capture all names, dates, handwritten notes, and tabular data without summarization or commentary.
    """

    response = client.models.generate_content(
        model=model_id,
        contents=[uploaded_file, prompt],
        config=types.GenerateContentConfig(
            system_instruction="You are a high-accuracy OCR assistant.",
        )
    )
    return response.text.strip()

def process_single_pdf(file_path, client, model_id, output_dir, output_format, overwrite=False, chunk_size=15):
    """Worker function to process a single PDF file, with chunking for large documents."""
    ocr_file = output_dir / f"{file_path.stem}.{output_format}"
    
    if ocr_file.exists() and not overwrite:
        print(f"  Skipping {file_path.name}: Output already exists.")
        return True

    print(f"\nProcessing: {file_path.name}")
    try:
        reader = PdfReader(file_path)
        num_pages = len(reader.pages)
        
        full_text = ""
        
        if num_pages <= chunk_size:
            # Process as a single file
            print(f"  Uploading {file_path.name} ({num_pages} pages)...")
            uploaded_file = client.files.upload(file=file_path)
            full_text = generate_ocr_for_file(client, model_id, uploaded_file)
        else:
            # Process in chunks
            print(f"  Large document detected: {num_pages} pages. Processing in chunks of {chunk_size}...")
            for i in range(0, num_pages, chunk_size):
                chunk_end = min(i + chunk_size, num_pages)
                print(f"    Processing pages {i+1} to {chunk_end}...")
                
                writer = PdfWriter()
                for page_num in range(i, chunk_end):
                    writer.add_page(reader.pages[page_num])
                
                with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
                    writer.write(temp_pdf)
                    temp_pdf_path = Path(temp_pdf.name)
                
                try:
                    uploaded_chunk = client.files.upload(file=temp_pdf_path)
                    chunk_text = generate_ocr_for_file(client, model_id, uploaded_chunk)
                    full_text += chunk_text + "\n\n"
                finally:
                    if temp_pdf_path.exists():
                        os.remove(temp_pdf_path)
        
        # Save OCR result
        with open(ocr_file, "w", encoding="utf-8") as f:
            f.write(full_text.strip())
        print(f"  Success! OCR saved: {file_path.name}")
        return True
    except Exception as e:
        print(f"  Error processing {file_path.name}: {e}")
        return False

def extract_pdf_text(input_folder, output_folder, output_format="txt", max_workers=5, overwrite=False, chunk_size=15):
    """
    Processes PDF files from a folder in parallel.
    """
    print(f"--- Starting Parallel PDF Text Extraction ({output_format}) ---")
    print(f"--- Max Workers: {max_workers} ---")
    print(f"--- Chunk Size: {chunk_size} ---")
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
            executor.submit(process_single_pdf, pdf, client, model_id, output_dir, output_format, overwrite, chunk_size) 
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
    parser.add_argument("-c", "--chunk-size", type=int, default=15, help="Number of pages per chunk for large documents (default: 15)")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing output files (default: False)")

    args = parser.parse_args()
    
    extract_pdf_text(
        args.input, 
        args.output, 
        output_format=args.format, 
        max_workers=args.workers, 
        overwrite=args.overwrite,
        chunk_size=args.chunk_size
    )
