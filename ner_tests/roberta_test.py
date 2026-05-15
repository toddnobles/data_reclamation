import torch
import csv
import re
from pathlib import Path
from transformers import pipeline

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

def chunk_text(text, max_chars=1500, overlap=200):
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

def run_ner_person_only(input_path):
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"--- Running Person-Only NER (RoBERTa) on {device.upper()} ---")
    
    # Load NER pipeline
    ner_pipe = pipeline(
        "ner", 
        model="Jean-Baptiste/roberta-large-ner-english", 
        aggregation_strategy="simple",
        device=0 if device == "mps" else -1
    )

    # Ensure output directory exists
    output_dir = Path("ner_tests/outputs/roberta_test")
    output_dir.mkdir(parents=True, exist_ok=True)

    path = Path(input_path)
    files = sorted(list(path.glob("*.md"))) if path.is_dir() else [path]

    if not files:
        print("No files found.")
        return

    for file_path in files:
        print(f"\nScanning: {file_path.name}")

        with open(file_path, "r", encoding="utf-8") as f:
            full_text = f.read()

        # Clean the text to convert HTML tables to Markdown and save tokens
        full_text = clean_markdown(full_text)

        # Split into chunks to fit RoBERTa's context window (usually 512 tokens)
        text_chunks = chunk_text(full_text)
        unique_results = {}

        for i, chunk in enumerate(text_chunks):
            if len(text_chunks) > 1:
                print(f"  Processing chunk {i+1}/{len(text_chunks)}...")
            
            # Run Inference
            entities = ner_pipe(chunk)

            # Filter for 'PER' (Person) entities
            person_entities = [ent for ent in entities if ent['entity_group'] == 'PER']

            for ent in person_entities:
                # Clean up any potential Markdown symbols like # or *
                name = ent['word'].strip().replace("#", "").replace("*", "")
                score = ent['score']

                # Remove individuals identified with only one character (ignoring periods)
                if len(name.replace(".", "")) <= 1:
                    continue
                
                if name not in unique_results or score > unique_results[name]:
                    unique_results[name] = score

        if not unique_results:
            print("No valid person entities detected.")
            continue

        # Print to Terminal
        print(f"{'PERSON NAME':<25} | {'CONFIDENCE'}")
        print("-" * 40)
        for name in sorted(unique_results.keys()):
            print(f"{name:<25} | {unique_results[name]:.2f}")

        # Save results to a CSV file for each file processed
        output_csv = output_dir / f"{file_path.stem}.csv"
        with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["PERSON NAME", "CONFIDENCE"])
            for name in sorted(unique_results.keys()):
                writer.writerow([name, f"{unique_results[name]:.4f}"])
        print(f"Results saved to {output_csv}")

if __name__ == "__main__":
    target = input("Enter file or folder path: ").strip()
    run_ner_person_only(target)
