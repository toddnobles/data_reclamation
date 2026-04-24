import torch
from pathlib import Path
from transformers import pipeline

def run_ner_person_only(input_path):
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"--- Running Person-Only NER on {device.upper()} ---")
    
    # Load NER pipeline
    ner_pipe = pipeline(
        "ner", 
        model="Jean-Baptiste/roberta-large-ner-english", 
        aggregation_strategy="simple",
        device=0 if device == "mps" else -1
    )

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

        # --- THE FILTERING LOGIC ---
        # We only keep entities where the group is 'PER'
        person_entities = [ent for ent in entities if ent['entity_group'] == 'PER']

        if not person_entities:
            print("No person entities found in this file.")
        else:
            print(f"{'PERSON NAME':<25} | {'CONFIDENCE'}")
            print("-" * 40)
            for ent in person_entities:
                # Clean up any potential Markdown symbols like # or *
                name = ent['word'].strip().replace("#", "").replace("*", "")
                print(f"{name:<25} | {ent['score']:.2f}")

if __name__ == "__main__":
    target = input("Enter file or folder path: ").strip()
    run_ner_person_only(target)