# PKTableLabelling

Extract Tables from PubMed OA datasets xml files, annotate these with prodigy annotation software and custom recipe. 

Get labelled json file from azure and split based on annotator for review session.  
```
python ./scripts/split_annotations.py --azure-file-name tableclass-trials-1-output.jsonl --save-local False
python ./scripts/split_annotations.py --azure-file-name tableclass-test-covs-100-output.jsonl --save-local False
python ./scripts/split_annotations.py --azure-file-name tableclass-test-params-100-output.jsonl --save-local False
python ./scripts/split_annotations.py --azure-file-name tableclass-test-params-250B-output.jsonl --save-local False
python ./scripts/split_annotations.py --azure-file-name tableclass-test-covs-250B-output.jsonl --save-local False
python ./scripts/split_annotations.py --azure-file-name tableclass-test-params-250A-output.jsonl --save-local False
python ./scripts/split_annotations.py --azure-file-name tableclass-test-covs-250A-output.jsonl --save-local False
```
Start Review Session
``` 
prodigy review final-covs100 tableclass-test-covs-100-gill,tableclass-test-covs-100-frank,tableclass-test-covs-100-joe,tableclass-test-covs-100-vicky -v choice  
prodigy review final-params100 tableclass-test-params-100-gill,tableclass-test-params-100-frank,tableclass-test-params-100-joe,tableclass-test-params-100-vicky -v choice
prodigy review midterm-covs250B tableclass-test-covs-100-palang,tableclass-test-covs-100-pum,tableclass-test-covs-100-frank,tableclass-test-covs-100-vicky -v choice  
```
Get Final Reviewed Annotations Out
```
python -m prodigy db-out final-covs100 > ./data/final-out//final-test-covs100.jsonl
python -m prodigy db-out final-params100 > ./data/final-out/final-test-params100.jsonl
```
