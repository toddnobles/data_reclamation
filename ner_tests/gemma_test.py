import os
import csv
import json
from pathlib import Path
from google import genai

def run_gemma_ner(input_path):
    print(f"--- Initializing Gemma 4 NER ---")
    
    # Load API Key
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not set.")
        return

    client = genai.Client(api_key=api_key)
    model_id = "gemma-4-31b-it"

    # Ensure output directory exists
    output_dir = Path("ner_tests/outputs/gemma_test")
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

        prompt = f"""
        Identify all unique individuals (person names) mentioned in the text below. 
        
        Text:
        {text}
        
        Return the results as a JSON list of objects, each with a 'name' key.
        Example: [ {{"name": "John Doe"}}, ... ]
        """

        try:
            response = client.models.generate_content(
                model=model_id,
                contents=prompt,
                config={
                    "response_mime_type": "application/json"
                }
            )
            
            # Parse the JSON response
            results = json.loads(response.text)
            
            if not results:
                print("No person entities detected.")
                continue

            # Extract names and deduplicate
            unique_names = sorted(list(set([entry.get('name', 'Unknown') for entry in results])))

            # Output Results to Terminal
            print(f"{'PERSON NAME'}")
            print("-" * 30)
            for name in unique_names:
                print(f"{name}")

            # Save to CSV
            output_csv = output_dir / f"{file_path.stem}.csv"
            with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["PERSON NAME"])
                for name in unique_names:
                    writer.writerow([name])
            
            print(f"Results saved to {output_csv}")

        except Exception as e:
            print(f"Error processing {file_path.name}: {e}")

if __name__ == "__main__":
    # Defaulting to the test_docs folder as requested
    target = "ner_tests/test_docs"
    run_gemma_ner(target)
