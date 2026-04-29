import torch
import csv
from pathlib import Path
from transformers import AutoTokenizer, pipeline
import nltk

nltk.download('punkt_tab')

def run_impresso_fixed_chunks(input_path):
    MODEL_NAME = "impresso-project/ner-stacked-bert-multilingual"
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    
    print(f"--- Initializing Impresso (Token-based Chunking) on {device.upper()} ---")
    
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    ner_pipe = pipeline(
        "generic-ner", 
        model=MODEL_NAME, 
        tokenizer=tokenizer, 
        trust_remote_code=True, 
        device=device
    )

    # Ensure output directory exists
    output_dir = Path("ner_tests/outputs/ner_stacked_bert_test")
    output_dir.mkdir(parents=True, exist_ok=True)

    path = Path(input_path)
    files = [path] if path.is_file() else list(path.glob("*.md"))

    if not files:
        print("No files found.")
        return

    for file_path in files:
        print(f"\nProcessing: {file_path.name}")
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        # TOKEN-BASED CHUNKING
        # Encode the entire text and split into 510 token segments (to leave room for special tokens)
        tokens = tokenizer.encode(text, add_special_tokens=False)
        chunk_size = 500 
        token_chunks = [tokens[i:i + chunk_size] for i in range(0, len(tokens), chunk_size)]
        
        # Decode tokens back to text chunks
        chunks = [tokenizer.decode(tc) for tc in token_chunks]
        
        all_person_entities = []
        found_labels = set()
        print(f"Document split into {len(chunks)} chunks based on token count.")

        for i, chunk in enumerate(chunks):
            if not chunk.strip(): continue
            
            try:
                results = ner_pipe(chunk)
                
                # Debug: Print raw results for the first chunk of the first file to see structure
                if i == 0:
                    print(f"--- Raw Sample Result (Chunk 0) ---")
                    print(results[:3] if isinstance(results, list) else results)
                
                if not results:
                    continue

                for ent in results:
                    # Impresso format uses 'type', 'surface', and 'confidence_ner'
                    if isinstance(ent, list):
                        items = ent
                    else:
                        items = [ent]

                    for item in items:
                        # Update keys based on raw sample: 'type' instead of 'label'
                        label = item.get('type') or item.get('entity_group') or item.get('label')
                        if label: found_labels.add(label)

                        # Target label is 'pers' based on sample
                        if label in ['pers', 'PER']:
                            name = item.get('surface') or item.get('word', "")
                            name = name.strip().replace("#", "").replace("*", "")

                            # Score key is 'confidence_ner'
                            score = item.get('confidence_ner') or item.get('score', 0)

                            # Convert score if it's a percentage (93.35 vs 0.93)
                            if score > 1:
                                score = score / 100.0

                            if len(name.replace(".", "")) > 1:
                                all_person_entities.append((name, float(score)))
            except Exception as e:
                print(f" Error in chunk {i}: {e}")

        # Output Results
        if not all_person_entities:
            print(f"No person entities detected. Found labels: {found_labels}")
        else:
            # Deduplicate results
            unique_results = {}
            for name, score in all_person_entities:
                if name not in unique_results or score > unique_results[name]:
                    unique_results[name] = score

            # Print to Terminal
            print(f"\n{'PERSON NAME':<30} | {'CONFIDENCE'}")
            print("-" * 45)
            for name in sorted(unique_results.keys()):
                print(f"{name:<30} | {unique_results[name]:.2f}")

            # Save results to a CSV file
            output_csv = output_dir / f"{file_path.stem}.csv"
            with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["PERSON NAME", "CONFIDENCE"])
                for name in sorted(unique_results.keys()):
                    writer.writerow([name, f"{unique_results[name]:.4f}"])
            print(f"Results saved to {output_csv}")

if __name__ == "__main__":
    target = input("Enter file or folder path: ").strip()
    run_impresso_fixed_chunks(target)
