#imports
import argparse
import pandas as pd
from prodigy.util import read_jsonl
from sklearn.metrics import cohen_kappa_score
from sklearn.preprocessing import MultiLabelBinarizer
from azure.storage.blob import BlobClient
from typing import Dict, List, Iterable
import numpy as np

def convert_labels(inp_labels: List[List[str]]):
    """Transforms labels to vector of binary numbers"""
    mlb = MultiLabelBinarizer(classes=(1,2,3,4,5,6))
    all_transformed_labels = mlb.fit_transform(inp_labels)
    all_transformed_labels = list(all_transformed_labels)
    # print(all_transformed_labels[1:4])
    return all_transformed_labels

mlb= MultiLabelBinarizer()

def sublists_to_dummies(f,sublist,index_key = None):
    '''Function to convert column containing lists to binary column for each label'''
    categories = [1,2,3,4,5]
    frame = pd.DataFrame(columns=categories)
    for d,i in f.iterrows():
        if type(i[sublist]) == list or np.array:
            try:
                if index_key != None:
                    key = i[index_key]
                    f =np.zeros(len(categories))
                    for j in i[sublist]:
                        f[categories.index(j)] = 1
                    if key in frame.index:
                        for j in i[sublist]:
                            frame.loc[key][j]+=1
                    else:
                        frame.loc[key]=f
                else:
                    f =np.zeros(len(categories))
                    for j in i[sublist]:
                        f[categories.index(j)] = 1
                    frame.loc[d]=f
            except:
                pass

    return frame

blob = BlobClient(
    account_url="https://pkpdaiannotations.blob.core.windows.net",
    container_name="pkpdaiannotations",
    blob_name="tableclass-test-params-100-output.jsonl",
    credential="UpC2SPFbEqJdY0tgY91y1oVe3ZcQwxALkJ2QIDTYN17FoTLmpltCFyzxKk13fjrp04y+7K4L6t5KR6VOMUKOqw==")

filename = "temp_annotations.jsonl"
with open(filename, "wb") as f:
    f.write(blob.download_blob().readall())

annotations = list(read_jsonl(filename))
uq_annotators = set([x["_session_id"] for x in annotations])

d= {}
for annotator in uq_annotators:
    sub_annotations = [an for an in annotations if an["_session_id"] == annotator]
    sub_df= pd.DataFrame(sub_annotations)
    final_df= sublists_to_dummies(sub_df, "accept", "text")
    d.update({str(annotator): final_df})

print(d)
#TODO: combine dfs for label columns from each annotator, pariwise


a=1
