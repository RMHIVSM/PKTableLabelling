# PKTableLabelling

Extract Tables from PubMed OA datasets xml files, annotate these with prodigy annotation software and custom recipe. 

Get labelled json file from azure and split based on annotator for review session.  
```
python ./scripts/split_annotations.py --azure-file-name tableclass-trials-1-output.jsonl --save-local False
```
Start Review Session
```
prodigy review final-trials tableclass-trials-1-ferran,tableclass-trials-1-gill,tableclass-trials-1-frank,tableclass-trials-1-joe -v choice  
```
