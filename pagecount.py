from pathlib import Path
from pypdf import PdfReader

def count_pdf_pages(directory):
    directory = Path(directory)
    total_pages = 0
    skipped_files = []

    for pdf_file in directory.rglob("*.pdf"):  # use glob("*.pdf") if no subfolders
        try:
            reader = PdfReader(pdf_file)
            num_pages = len(reader.pages)
            total_pages += num_pages
            print(f"{pdf_file.name}: {num_pages} pages")
        except Exception as e:
            print(f"Skipping {pdf_file.name} due to error: {e}")
            skipped_files.append(pdf_file.name)

    print("\n--- Summary ---")
    print(f"Total pages: {total_pages}")
    print(f"Total PDFs processed: {len(list(directory.rglob('*.pdf')))}")

    if skipped_files:
        print("\nSkipped files:")
        for f in skipped_files:
            print(f" - {f}")

    return total_pages


if __name__ == "__main__":
    folder_path = "/Users/toddnobles/Documents/data_reclamation/examples"  # <-- change this
    count_pdf_pages(folder_path)
