# Run Prodigy Locally

Installation instructions - from command line 

Confirm python is installed 
```
python
```
To install python (skip if not needed)
```
https://www.python.org/downloads/windows/
```
Confirm pip is installed 
```
pip help
```

To install pip (skip if not needed)
```
python get-pip.py
#verify installation
pip -V
```

To Install all python packages needed 
```
pip install .
```

Install prodigy
```
pip install <prodigy-dir>/prodigy-<version>.whl 
```
## Run recipe locally  
```
python -m prodigy label-json tables_trial_labels data/json/pmctables.jsonl -F recipe/label-json.py
```
## Get annotations out 

```
python -m prodigy db-out tables_trial_labels > ./output_annotations.jsonl
```


