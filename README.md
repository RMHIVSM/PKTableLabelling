# PKTableLabelling

Extract Tables from PubMed OA datasets xml files, annotate these with prodigy annotation software and custom recipe. 

Get labelled json file from azure and split based on annotator for review session.  
```
python ./scripts/split_annotations.py --azure-file-name tableclass-trials-1-output.jsonl --save-local False
python ./scripts/split_annotations.py --azure-file-name tableclass-test-covs-100-output.jsonl --save-local False
python ./scripts/split_annotations.py --azure-file-name tableclass-test-params-100-output.jsonl --save-local False
```
Start Review Session
```
prodigy review final-trials tableclass-trials-1-ferran,tableclass-trials-1-gill,tableclass-trials-1-frank,tableclass-trials-1-joe -v choice  
prodigy review final-covs100 tableclass-test-covs-100-ferran,tableclass-test-covs-100-gill,tableclass-test-covs-100-frank,tableclass-test-covs-100-joe,tableclass-test-covs-100-vicky -v choice  
prodigy review final-params100 tableclass-test-params-100-ferran,tableclass-test-params-100-gill,tableclass-test-params-100-frank,tableclass-test-params-100-joe,tableclass-test-params-100-vicky -v choice  
```
