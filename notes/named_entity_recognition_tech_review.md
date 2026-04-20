## Overview
Goal is to find a way to identify individuals within the extracted text from the archive scans. 

## Option 1 Impresso ner stacked bert
- [impresso-project/ner-stacked-bert-multilingual · Hugging Face](https://huggingface.co/impresso-project/ner-stacked-bert-multilingual)
- **Pros**: Trained specifically for historical document processing from relevant time period. Creators state that "These additional Transformer layers help in mitigating the effects of OCR noise, spelling variation, and non-standard linguistic usage found in historical documents."
- **Cons**: Looks like their evaluations were done using German and French, but they included English in the training set
- **Demo:** [Multilingual Named Entity Recognition - a Hugging Face Space by impresso-project](https://huggingface.co/spaces/impresso-project/multilingual-named-entity-recognition)
- **Notes:**  Impresso project has an interesting set of tools for historical OCR and text processing [Title Unavailable \| Site Unreachable](https://impresso-project.ch/datalab/)

## Option 2 hmBert
- [hmBERT: Historical Multilingual Language Models for Named Entity Recognition](https://arxiv.org/pdf/2205.15575)
- **Description**: Built specifically for using OCRd text. For English part of training set they used digitized books from British library from 1800-1900. 
- **Pros**: trained on historical OCRd text from correct period
- **Cons**: 

## Option 3 GLiNER
- **Description**: describes itself as BERT-like. They highlight better zero-shot performance compared to LLMs and ability to recognize any entity type as a benefit over other NER techniques
- **Pros**: good documentation. fine tuning instructions available [Training - Home 0.2.24 documentation](https://urchade.github.io/GLiNER/training.html). 
- **Cons**: No clear cons. The smaller demo space I tried seemed to have a context window where it wouldn't recognize names towards the end of the text I tested it with. 
- Huggingface demo: [GLiNER HandyLab - a Hugging Face Space by knowledgator](https://huggingface.co/spaces/knowledgator/GLiNER_HandyLab) 


## Option 4 spaCy
- [Named Entity Recognition (NER) using spaCy · spaCy Universe](https://spacy.io/universe/project/video-spacys-ner-model-alt)
	- [Chapter 1: Finding words, phrases, names and concepts · Advanced NLP with spaCy](https://course.spacy.io/en/chapter1)
- **Description:** 
- **Pros:** Lots of documentation and tutorials. 
- **Cons:** Trained on modern web text 

## Option 5
- structure output from a newer llm like Gemma4 

## Resources

Here's a leaderboard for various named entity recognition approaches. It seems a bit outdated but saving for future reference. [Named entity recognition \| NLP-progress](https://nlpprogress.com/english/named_entity_recognition.html). Most if not all of these evaluations were on modern text datasets.****