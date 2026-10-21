import csv
import string
import argparse
from pathlib import Path
import rapidfuzz
from rapidfuzz import process, fuzz
from rapidfuzz.distance import Levenshtein

def load_names(file_path):
    """Loads and normalizes names from a CSV file, detecting the header."""
    if not file_path.exists():
        return []
    
    names = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            return []
            
        # Create a mapping of {normalized_name: original_name}
        # Example: {"personname": "person_name"}
        header_map = {h.lower().replace("_", "").replace(" ", ""): h for h in reader.fieldnames}
        
        # Look for the normalized version of common name columns
        actual_header = header_map.get("personname")
        
        # If not found, check for other common names like 'name'
        if not actual_header:
            actual_header = header_map.get("name")
            
        # Fallback to the first column if no known header is found
        if not actual_header:
            actual_header = reader.fieldnames[0]

        for row in reader:
            val = row.get(actual_header)
            if val:
                name = rapidfuzz.utils.default_process(val)
                name = " ".join(name.split())
                if name:
                    names.append(name)
                
    return list(set(names))

def calculate_matches(gt_names, out_names, threshold):
    """
    Uses rapidfuzz to find a 1-to-1 matching between GT and Output.
    """
    # if either empty then no matches. 
    if not gt_names or not out_names:
        return 0, len(gt_names), len(out_names)

    # 1. Exact Matches
    gt_set = set(gt_names)
    out_set = set(out_names)
    exact_matches = gt_set.intersection(out_set)
    
    tp_count = len(exact_matches)
    remaining_gt = [n for n in gt_names if n not in exact_matches]
    remaining_out = [n for n in out_names if n not in exact_matches]

    if threshold > 0 and remaining_gt and remaining_out:
        # 2. Fuzzy Matches using rapidfuzz cdist 
        # cdist returns a matrix where distances[i][j] is dist(remaining_gt[i], remaining_out[j])
        distances = process.cdist(remaining_gt, remaining_out, scorer=Levenshtein.distance)
        
        # Flatten and filter by threshold
        potential_matches = []
        for i, row in enumerate(distances):
            for j, dist in enumerate(row):
                if dist <= threshold:
                    potential_matches.append((dist, i, j))
        
        # Sort by distance (greedy best match)
        potential_matches.sort()
        
        used_gt = set()
        used_out = set()
        for dist, i, j in potential_matches:
            if i not in used_gt and j not in used_out:
                tp_count += 1
                used_gt.add(i)
                used_out.add(j)

    fn_count = len(gt_names) - tp_count
    fp_count = len(out_names) - tp_count
    
    return tp_count, fn_count, fp_count

def run_evaluation(gt_dir, out_dir, threshold, title):
    gt_dir = Path(gt_dir)
    out_dir = Path(out_dir)
    
    if not gt_dir.exists():
        print(f"Error: Ground truth directory {gt_dir} not found.")
        return
    if not out_dir.exists():
        print(f"Error: Comparison directory {out_dir} not found.")
        return

    gt_files = sorted(list(gt_dir.glob("*.csv")))
    if not gt_files:
        print(f"No CSV files found in {gt_dir}")
        return

    print(f"\n--- {title} ---")
    print(f"Reference:  {gt_dir}")
    print(f"Comparison: {out_dir}")
    print(f"Distance Threshold: {threshold}")
    print("-" * 145)
    print(f"{'FILE':<75} | {'MATCH (TP)':<12} | {'MISS (FN)':<12} | {'ERROR (FP)':<12} | {'RECALL':<8} | {'PRECISION':<8}")
    print("-" * 145)

    total_tp, total_fn, total_fp = 0, 0, 0
    doc_recalls = []
    doc_precisions = []

    for gt_file in gt_files:
        out_file = out_dir / gt_file.name
        if not out_file.exists():
            # If output file is missing, all GT names are missed
            gt_names = load_names(gt_file)
            tp, fn, fp = 0, len(gt_names), 0
        else:
            gt_names = load_names(gt_file)
            out_names = load_names(out_file)
            tp, fn, fp = calculate_matches(gt_names, out_names, threshold)

        total_tp += tp
        total_fn += fn
        total_fp += fp

        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        
        doc_recalls.append(recall)
        doc_precisions.append(precision)
        
        print(f"{gt_file.stem:<75} | {tp:<12} | {fn:<12} | {fp:<12} | {recall:>8.1%} | {precision:>8.1%}")

    print("-" * 145)
    overall_recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0
    overall_precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
    overall_f1 = 2 * (overall_precision * overall_recall) / (overall_precision + overall_recall) if (overall_precision + overall_recall) > 0 else 0

    avg_doc_recall = sum(doc_recalls) / len(doc_recalls) if doc_recalls else 0
    avg_doc_precision = sum(doc_precisions) / len(doc_precisions) if doc_precisions else 0
    avg_f1 = 2 * (avg_doc_precision * avg_doc_recall) / (avg_doc_precision + avg_doc_recall) if (avg_doc_precision + avg_doc_recall) > 0 else 0

    print(f"{'OVERALL TOTALS':<75} | {total_tp:<12} | {total_fn:<12} | {total_fp:<12} | {overall_recall:>8.1%} | {overall_precision:>8.1%}")
    print(f"{'AVERAGE DOCUMENT SCORES':<75} | {'-':<12} | {'-':<12} | {'-':<12} | {avg_doc_recall:>8.1%} | {avg_doc_precision:>8.1%}")
    print("-" * 145)
    print(f"Overall F1-Score (Corpus): {overall_f1:.2%}")
    print(f"Average F1-Score (Doc):    {avg_f1:.2%}")

def select_from_list(items, title, prompt):
    if not items:
        return None
    print(f"\n{title}:")
    for idx, item in enumerate(items):
        print(f" {idx+1}. {item}")
    
    choice = input(f"\n{prompt}: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(items):
        return items[int(choice)-1]
    return choice

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NER Evaluation using RapidFuzz")
    parser.add_argument("-m", "--model", help="Model name (e.g., gemma_test)")
    parser.add_argument("-g", "--gt", help="Ground truth subfolder (e.g., eden_gts)")
    parser.add_argument("--compare", action="store_true", help="Compare two ground truth sets instead of model vs GT")
    parser.add_argument("--threshold", type=int, default=2, help="Levenshtein distance threshold (default: 2)")
    
    args = parser.parse_args()

    gt_base_path = Path("ner_tests/undergrad_ground_truths")
    outputs_path = Path("ner_tests/outputs")

    if args.compare:
        # Inter-Annotator Agreement Mode
        available_gts = sorted([d.name for d in gt_base_path.iterdir() if d.is_dir()])
        
        gt1 = args.gt or select_from_list(available_gts, "Select Ground Truth Set 1 (Reference)", "Select number or type name")
        if not gt1:
            print("Error: No reference ground truth selected.")
            exit(1)
            
        gt2 = args.model or select_from_list(available_gts, "Select Ground Truth Set 2 (Comparison)", "Select number or type name")
        if not gt2:
            print("Error: No comparison ground truth selected.")
            exit(1)

        run_evaluation(gt_base_path / gt1, gt_base_path / gt2, args.threshold, f"Inter-Annotator Agreement: {gt1} vs {gt2}")
    
    else:
        # Standard Model vs GT Mode
        # 1. Select Model
        selected_model = args.model
        if not selected_model:
            available_models = sorted([d.name for d in outputs_path.iterdir() if d.is_dir()])
            selected_model = select_from_list(available_models, "Available Models", "Select a model number or type the name")
        
        if not selected_model:
            print("Error: No model selected.")
            exit(1)

        # 2. Select Ground Truth
        selected_gt = args.gt
        if not selected_gt:
            available_gts = sorted([d.name for d in gt_base_path.iterdir() if d.is_dir()])
            selected_gt = select_from_list(available_gts, "Available Ground Truth Sets", "Select a ground truth set number or type the name")

        if not selected_gt:
            print("Error: No ground truth set selected.")
            exit(1)

        run_evaluation(gt_base_path / selected_gt, outputs_path / selected_model, args.threshold, f"RapidFuzz NER Evaluation: {selected_model}")
