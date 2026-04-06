# Data Reclamation

This repository contains the code for running publicly available boarding school related documents through the olmocr pipeline and creating an online viewer. 

- **olmocr_cirrascale.py**: Uses the Cirrascale API to extract the text and formatting from the pdf stored in the **examples** folder. 
- **generate_manifest.py**: Pairs the extracted text in markdown format with the original PDF files for viewing in the **index.html** which is published on [Github pages](https://toddnobles.github.io/data_reclamation/)


To view locally before pushing to Github pages, run the following:
- python3 -m http.server 8000
- Then open [http://localhost:8000](http://localhost:8000) in your browser.