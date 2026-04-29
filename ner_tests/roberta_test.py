import torch
import csv
from pathlib import Path
from transformers import pipeline

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
    files = [path] if path.is_file() else list(path.glob("*.md"))

    if not files:
        print("No files found.")
        return

    for file_path in files:
        print(f"\nScanning: {file_path.name}")

        with open(file_path, "r", encoding="utf-8") as f:
            md_content = f.read()

        # Run Inference
        entities = ner_pipe(md_content)

        # Filter for 'PER' (Person) entities
        person_entities = [ent for ent in entities if ent['entity_group'] == 'PER']

        if not person_entities:
            print("No person entities found in this file.")
        else:
            # Deduplicate results, keeping highest confidence
            unique_results = {}
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
                print("No valid person entities detected after filtering.")
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
