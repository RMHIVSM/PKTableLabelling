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
python ./scripts/split_annotations.py --azure-file-name tableclass-test-params-200A-output.jsonl --save-local False
python ./scripts/split_annotations.py --azure-file-name tableclass-test-covs-200A-output.jsonl --save-local False
python ./scripts/split_annotations.py --azure-file-name tableclass-test-params-200B-output.jsonl --save-local False
python ./scripts/split_annotations.py --azure-file-name tableclass-test-covs-200B-output.jsonl --save-local False
```
Start Review Session
``` 
prodigy review final-covs100 tableclass-test-covs-100-gill,tableclass-test-covs-100-frank,tableclass-test-covs-100-joe,tableclass-test-covs-100-vicky -v choice  
prodigy review final-params100 tableclass-test-params-100-gill,tableclass-test-params-100-frank,tableclass-test-params-100-joe,tableclass-test-params-100-vicky -v choice
prodigy review final-covs250B tableclass-test-covs-250B-vicky,tableclass-test-covs-250B-pum,tableclass-test-covs-250B-frank,tableclass-test-covs-250B-palang -v choice
prodigy review final-params250B tableclass-test-params-250B-vicky,tableclass-test-params-250B-pum,tableclass-test-params-250B-frank,tableclass-test-params-250B-palang -v choice 
prodigy review final-params250A tableclass-test-params-250A-vicky,tableclass-test-params-250A-gill,tableclass-test-params-250A-joe -v choice
prodigy review final-covs250A tableclass-test-covs-250A-vicky,tableclass-test-covs-250A-gill,tableclass-test-covs-250A-joe -v choice   
prodigy review final-params200B tableclass-test-params-200B-vicky,tableclass-test-params-200B-pum,tableclass-test-params-200B-palang,tableclass-test-params-200B-frank -v choice
prodigy review final-covs200B tableclass-test-covs-200B-vicky,tableclass-test-covs-200B-pum,tableclass-test-covs-200B-palang,tableclass-test-covs-200B-frank -v choice   
prodigy review final-params200A tableclass-test-params-200A-vicky,tableclass-test-params-200A-gill,tableclass-test-params-200A-joe,tableclass-test-params-200A-frank -v choice
prodigy review final-covs200A tableclass-test-covs-200A-vicky,tableclass-test-covs-200A-gill,tableclass-test-covs-200A-joe,tableclass-test-covs-200A-frank -v choice   
```
Get Final Reviewed Annotations Out
```
python -m prodigy db-out final-covs100 > ./data/final-out//final-test-covs100.jsonl
python -m prodigy db-out final-params100 > ./data/final-out/final-test-params100.jsonl
python -m prodigy db-out final-covs200B > ./data/final-out//final-test-covs200B.jsonl
python -m prodigy db-out final-params200B > ./data/final-out/final-test-params200B.jsonl
python -m prodigy db-out final-covs250B > ./data/final-out//final-test-covs250B.jsonl
python -m prodigy db-out final-params250B > ./data/final-out/final-test-params250B.jsonl
python -m prodigy db-out final-covs250A > ./data/final-out//final-test-covs250A.jsonl
python -m prodigy db-out final-params250A > ./data/final-out/final-test-params250A.jsonl
```
