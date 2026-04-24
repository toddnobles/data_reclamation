import torch
from pathlib import Path
from flair.data import Sentence
from flair.nn import Classifier

def run_flair_ner(input_path):
    # Determine device
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"--- Initializing Flair (ner-large)---")
    
    # Load the NER tagger
    tagger = Classifier.load('ner-large')
    
    path = Path(input_path)
    files = [path] if path.is_file() else list(path.glob("*.md"))

    if not files:
        print("No files found.")
        return

    for file_path in files:
        print(f"\nProcessing: {file_path.name}")
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Direct processing of full text
        sentence = Sentence(text)
        tagger.predict(sentence)
        
        all_person_entities = []
        
        # Iterate over entities found
        for entity in sentence.get_labels('ner'):
            if entity.value == 'PER':
                name = entity.data_point.text
                score = entity.score
                all_person_entities.append((name, score))

        # Output Results
        if not all_person_entities:
            print("No person entities detected.")
        else:
            # Deduplicate results, keeping highest confidence
            unique_results = {}
            for name, score in all_person_entities:
                # Clean name: remove markdown artifacts
                clean_name = name.strip().replace("#", "").replace("*", "")
                if len(clean_name.replace(".", "")) <= 1:
                    continue
                    
                if clean_name not in unique_results or score > unique_results[clean_name]:
                    unique_results[clean_name] = score

            print(f"\n{'PERSON NAME':<30} | {'CONFIDENCE'}")
            print("-" * 45)
            for name in sorted(unique_results.keys()):
                print(f"{name:<30} | {unique_results[name]:.2f}")

if __name__ == "__main__":
    target = input("Enter file or folder path: ").strip()
    run_flair_ner(target)
