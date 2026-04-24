import torch
from pathlib import Path
from transformers import AutoTokenizer, pipeline
import nltk

nltk.download('punkt_tab')


def run_impresso_fixed_chunks(input_path):
    MODEL_NAME = "impresso-project/ner-stacked-bert-multilingual"
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    
    print(f"--- Initializing Impresso (Chunked Mode) on {device.upper()} ---")
    
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    tokenizer.model_max_length = 512 * 100  # Suppress warnings during manual chunking
    ner_pipe = pipeline(
        "generic-ner", 
        model=MODEL_NAME, 
        tokenizer=tokenizer, 
        trust_remote_code=True, 
        device=device
    )

    path = Path(input_path)
    files = [path] if path.is_file() else list(path.glob("*.md"))

    for file_path in files:
        print(f"\nProcessing: {file_path.name}")
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        # IMPROVED CHUNKING LOGIC:
        # 1. Split into sentences
        # 2. Group sentences into chunks < 512 tokens
        # 3. Handle cases where a single sentence is too long
        sentences = nltk.sent_tokenize(text)
        chunks = []
        current_chunk = []
        current_length = 0
        
        # We target ~400 tokens to be very safe
        max_chunk_tokens = 400 

        for sent in sentences:
            # We use a large enough model_max_length to avoid warnings during chunking
            sent_tokens = tokenizer.encode(sent, add_special_tokens=False, truncation=False)
            
            # If a single sentence is too long, split it by words
            if len(sent_tokens) > max_chunk_tokens:
                if current_chunk:
                    chunks.append(" ".join(current_chunk))
                    current_chunk = []
                    current_length = 0
                
                # Split long sentence by words
                words = sent.split()
                sub_chunk = []
                sub_length = 0
                for word in words:
                    word_tokens = tokenizer.encode(word, add_special_tokens=False)
                    if sub_length + len(word_tokens) > max_chunk_tokens:
                        chunks.append(" ".join(sub_chunk))
                        sub_chunk = [word]
                        sub_length = len(word_tokens)
                    else:
                        sub_chunk.append(word)
                        sub_length += len(word_tokens)
                if sub_chunk:
                    chunks.append(" ".join(sub_chunk))
                continue

            if current_length + len(sent_tokens) > max_chunk_tokens:
                if current_chunk:
                    chunks.append(" ".join(current_chunk))
                current_chunk = [sent]
                current_length = len(sent_tokens)
            else:
                current_chunk.append(sent)
                current_length += len(sent_tokens)
        
        if current_chunk:
            chunks.append(" ".join(current_chunk))
        
        all_person_entities = []
        print(f"Document split into {len(chunks)} chunks based on token count.")

        for i, chunk in enumerate(chunks):
            if not chunk.strip(): continue
            
            try:
                results = ner_pipe(chunk)
                
                for ent in results:
                    # Impresso uses 'type' instead of 'entity_group' or 'label'
                    # and 'surface' instead of 'word'
                    label = ent.get('type') or ent.get('entity_group') or ent.get('label')
                    
                    if label in ['pers', 'PER']:
                        word = ent.get('surface') or ent.get('word') or ent.get('text')
                        if word:
                            word = str(word).strip().replace("#", "")
                            if len(word.replace(".", "")) > 1:
                                score = ent.get('confidence_ner') or ent.get('score', 0)
                                all_person_entities.append((word, float(score)))
            except Exception as e:
                print(f" Error in chunk {i}: {e}")

        # Output Results
        if not all_person_entities:
            print("No person entities detected.")
        else:
            # Deduplicate results
            unique_results = {}
            for name, score in all_person_entities:
                if name not in unique_results or score > unique_results[name]:
                    unique_results[name] = score

            print(f"\n{'PERSON NAME':<30} | {'CONFIDENCE'}")
            print("-" * 45)
            for name in sorted(unique_results.keys()):
                print(f"{name:<30} | {unique_results[name]:.2f}")

if __name__ == "__main__":
    target = input("Enter file or folder path: ").strip()
    run_impresso_fixed_chunks(target)