# Psuedocoded main script for processing documents 

Assuming we get access to the files via a remote connection, this script needs to accomplish the following: 

## Option 1: Hyak
1. once logged in to the remote server ssh into hyak. 
1.5 start separate compute node that monitors the export folder and communicates with me about things that are broken
1.75 could start a new 
bash Script starts here 
1. Upload files  
2. run documents through the olmocr pipeline
    - create a folder with access privileges to only me
    - upload docs to a folder on gscratch
    - run through olmocr pipeline using a slurm job request 
    - once this is done things live in the output folders on gscratch on Hyak.
    - check done flags for docs that didn't process 
        - human check step to see why these didn't process (can have it email me with info about the file)
    - save model outputs locally. Just grab the full workspace folder which contains md, jsonl, and done_flags.
    - Run NER using TBD model (either Gemma4 or Flair)
        - Gemma involves a second Slurm job request 
    - create sample priority number for all files in the corpus
        enumerate all files, shuffle of pdf files 
    - create a to_be_checked folder of the following structure: (This step could happen on hyak or in Puyallup environment)
        - RA 1 
            - folder of original pdfs/
            - folder of blank csv for each file
        - RA 2
            -  folder of original pdfs
            - folder with blank csv for each file 
    - delete pdfs and model outputs 
        


## Option 2: cirrascale
Same as above, but minus one ssh and no need to worry about deleting files after completion. Sampling would be done within the first ssh environment on Puyallup compute. 