import csv
import string
from pathlib import Path

def load_names(file_path):
    """Loads names from a CSV and returns a normalized set (lowercase, no whitespace, no punctuation)."""
    names = set()
    if not file_path.exists():
        return names
    
    # Create a translation table to remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Normalize: lowercase, strip whitespace, and remove punctuation
            name = row["PERSON NAME"].strip().lower().translate(translator)
            if name:
                names.add(name)
    return names

def evaluate(model_folder):
    gt_dir = Path("ner_tests/ground_truth")
    out_dir = Path("ner_tests/outputs") / model_folder
    
    if not out_dir.exists():
        print(f"Error: Model output directory '{out_dir}' not found.")
        return

    gt_files = list(gt_dir.glob("*.csv"))
    
    if not gt_files:
        print("No ground truth files found in ner_tests/ground_truth.")
        return

    print(f"\nEvaluating: {model_folder}")
    print(f"{'FILE':<30} | {'MATCH'} | {'MISSED'} | {'EXTRA'} | {'RECALL'}")
    print("-" * 75)

    total_tp = 0
    total_fn = 0
    total_fp = 0

    for gt_file in sorted(gt_files):
        out_file = out_dir / gt_file.name
        
        gt_names = load_names(gt_file)
        out_names = load_names(out_file)
        
        if not gt_names and not out_names:
            continue

        # Comparisons
        true_positives = gt_names.intersection(out_names)
        false_negatives = gt_names - out_names  # In GT but not in Output
        false_positives = out_names - gt_names  # In Output but not in GT
        
        # Calculate Recall (How much of the truth did we find?)
        recall = len(true_positives) / len(gt_names) if len(gt_names) > 0 else 0
        
        total_tp += len(true_positives)
        total_fn += len(false_negatives)
        total_fp += len(false_positives)

        print(f"{gt_file.stem:<30} | {len(true_positives):<5} | {len(false_negatives):<6} | {len(false_positives):<5} | {recall:.2%}")

    # Overall Summary
    print("-" * 75)
    overall_recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0
    overall_precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
    
    print(f"{'OVERALL':<30} | {total_tp:<5} | {total_fn:<6} | {total_fp:<5} | {overall_recall:.2%}")
    print(f"\nOverall Precision: {overall_precision:.2%}")
    print(f"Overall Recall:    {overall_recall:.2%}")
    print("\nPrecision: % of model's guesses that were correct (True Positives / (True Positives + False Positives))")
    print("Recall:    % of actual names the model found (True Positives / (True Positives + False Negatives))")

if __name__ == "__main__":
    # List available model outputs
    outputs_path = Path("ner_tests/outputs")
    available_models = [d.name for d in outputs_path.iterdir() if d.is_dir()]
    
    if not available_models:
        print("No model outputs found in ner_tests/outputs/")
    else:
        print("Available models:")
        for idx, model in enumerate(available_models):
            print(f"{idx + 1}. {model}")
        
        choice = input("\nEnter the number or name of the model to evaluate: ").strip()
        
        if choice.isdigit() and 1 <= int(choice) <= len(available_models):
            model_to_eval = available_models[int(choice) - 1]
        else:
            model_to_eval = choice
            
        evaluate(model_to_eval)
