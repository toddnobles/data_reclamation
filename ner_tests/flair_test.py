import torch
import csv
from pathlib import Path
from flair.data import Sentence
from flair.nn import Classifier

def run_flair_ner(input_path):
    # mps apparently faster so using that here if available, but fallback to cpu if not
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"--- Initializing Flair (ner-large)---")
    
    # Load the NER tagger from the flair library
    tagger = Classifier.load('ner-large')
    
    # Ensure output directory exists
    output_dir = Path("ner_tests/outputs/flair_test")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    path = Path(input_path)
    # take single file or list of files to process
    files = [path] if path.is_file() else list(path.glob("*.md"))

    
    if not files:
        print("No files found.")
        return

    # Loop through files procesing each one and extracting person entities
    for file_path in files:
        print(f"\nProcessing: {file_path.name}")
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Direct processing of full text
        sentence = Sentence(text) # converts to a flair Sentence object
        tagger.predict(sentence) # tags all entties in the sentence (person and non-person)
        
        all_person_entities = []
        
        # Iterate over entities found and store the peerson entities with their confidence scores
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
                # requires at least 2 characters after cleaning to be considered a valid name. Handles things like just a single J.
                #if len(clean_name.replace(".", "")) <= 1:
                #    continue
                    
                if clean_name not in unique_results or score > unique_results[clean_name]:
                    unique_results[clean_name] = score

            print(f"\n{'PERSON NAME':<30} | {'CONFIDENCE'}")
            print("-" * 45)
            for name in sorted(unique_results.keys()):
                print(f"{name:<30} | {unique_results[name]:.2f}")

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
    run_flair_ner(target)
