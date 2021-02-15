import prodigy
from prodigy.components.loaders import JSONL

OPTIONS = [
        {"id": 0, "text": "Non-compartmental Parameters"},
        {"id": 1, "text": "Compartmental Parameters"},
        {"id": 2, "text": "PBPK Parameters"},
        {"id": 3, "text": "PK Concentrations/Observations"},
        {"id": 4, "text": "Unclear (Parameters)"},
        {"id": 5, "text": "Covariates (Demographics)"},
        {"id": 6, "text": "Covariates (Doses)"}
        {"id": 7, "text": "Covariates (Number of Samples)"}
        {"id": 8, "text": "Covariates (Other)"},
        {"id": 9, "text": "Not Relevant"},

]
#
@prodigy.recipe("label-json")

def label_json(dataset, html_path):
    """Stream in json tables from a directory and label them from fixed field"""

    return {
        "dataset": dataset,
        "stream": get_stream(html_path),
        "view_id": "choice",
        "config": {
            "choice_style": "multiple",  # or "single"
            # Automatically accept and submit the answer if an option is
            # selected (only available for single-choice tasks)
            #"choice_auto_accept": True,
            "global_css": ".prodigy-button-reject, .prodigy-button-ignore {display: none}",
            "custom_theme": {"cardMinWidth": 300, "cardMaxWidth": 1500, "smallText": 15},
            "instructions": "./recipes/vicky/label-json-instructions.html",
        }
    }

def get_stream(html_path):
        # Load the directory of images and add options to each task

    stream = JSONL(html_path)

    for eg in stream:
        eg["options"] = OPTIONS
        yield eg
