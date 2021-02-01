import prodigy
from prodigy.components.loaders import JSONL

OPTIONS = [
        {"id": 0, "text": "PK Parameters"},
        {"id": 1, "text": "Covariates"},
        {"id": 2, "text": "Other"}, 
        {"id": 3, "text": "Unclear"}
]

@prodigy.recipe("label-json")
 
def label_html(dataset, html_path):
     #Stream in htmls from a directory and label them from fixed field

    return {
        "dataset": dataset,
        "stream": get_stream(html_path),
        "view_id": "choice",
        "config": {
            "choice_style": "single",  # or "multiple"
            # Automatically accept and submit the answer if an option is
            # selected (only available for single-choice tasks)
            #"choice_auto_accept": True,
            "global_css": ".prodigy-button-reject, .prodigy-button-ignore {display: none}",
        }
    }

def get_stream(html_path):
        # Load the directory of images and add options to each task

    stream = JSONL(html_path)

    for eg in stream:
        eg["options"] = OPTIONS
        yield eg
