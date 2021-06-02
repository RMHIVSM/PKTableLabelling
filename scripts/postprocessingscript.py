#imports
import pandas as pd
import jsonlines

with jsonlines.open("../data/out/tableclass-trials-1-output.jsonl") as reader:
    json_list = []
    for obj in reader:
        json_list.append(obj)

df = pd.DataFrame.from_dict(json_list)
df.head()
