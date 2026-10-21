import subprocess
import re
from pathlib import Path

def run_eval(ref, comp, is_compare=False):
    """
    Runs ner_evaluation_rapidfuzz.py and parses the summary statistics from the output.
    """
    cmd = ["python", "ner_evaluation_rapidfuzz.py"]
    if is_compare:
        # Inter-Annotator Agreement mode (GT vs GT)
        cmd += ["--compare", "-g", ref, "-m", comp]
    else:
        # Standard mode (Model vs GT)
        cmd += ["-m", ref, "-g", comp]
    
    cmd += ["--threshold", "2"]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout
    
    # Extract Corpus-wide scores (from the OVERALL TOTALS line)
    # This line contains: MATCH (TP) | MISS (FN) | ERROR (FP) | RECALL | PRECISION
    totals_line = re.search(r"OVERALL TOTALS\s+\|.*?\|.*?\|.*?\|\s+([\d.]+)%\s+\|\s+([\d.]+)%", output)
    f1_corpus = re.search(r"Overall F1-Score \(Corpus\):\s+([\d.]+)%", output)
    
    # Extract Average Document scores
    f1_doc = re.search(r"Average F1-Score \(Doc\):\s+([\d.]+)%", output)
    avg_scores_line = re.search(r"AVERAGE DOCUMENT SCORES\s+\|.*?\|.*?\|.*?\|\s+([\d.]+)%\s+\|\s+([\d.]+)%", output)
    
    return {
        "recall_total": totals_line.group(1) if totals_line else "N/A",
        "precision_total": totals_line.group(2) if totals_line else "N/A",
        "f1_corpus": f1_corpus.group(1) if f1_corpus else "N/A",
        "recall_avg": avg_scores_line.group(1) if avg_scores_line else "N/A",
        "precision_avg": avg_scores_line.group(2) if avg_scores_line else "N/A",
        "f1_doc": f1_doc.group(1) if f1_doc else "N/A"
    }

models = [
    "flair_test", 
    "flair_test_gemma_ocr", 
    "gemma_test", 
    "gemma_test_gemma_ocr"
]

gt_sets = ["eden_gts", "marina_gts"]

# Print Markdown Table Header
# We include both Corpus-wide (Totals) and Document-level (Averages) to be explicit
print(f"| Model / Comparison | GT Set (Ref) | Recall (Total) | Precision (Total) | F1 (Corpus Total) | F1 (Doc Avg) |")
print(f"| :--- | :--- | :--- | :--- | :--- | :--- |")

# 1. Run Model Evaluations
for model in models:
    for gt in gt_sets:
        scores = run_eval(model, gt)
        print(f"| {model} | {gt} | {scores['recall_total']}% | {scores['precision_total']}% | {scores['f1_corpus']}% | {scores['f1_doc']}% |")

# 2. Run Inter-Annotator Agreement (Human Baseline)
iaa = run_eval("eden_gts", "marina_gts", is_compare=True)
print(f"| **IAA: Eden vs Marina** | eden_gts | {iaa['recall_total']}% | {iaa['precision_total']}% | **{iaa['f1_corpus']}%** | **{iaa['f1_doc']}%** |")
