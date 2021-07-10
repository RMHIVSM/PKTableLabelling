# imports
import argparse
import pandas as pd
from prodigy.util import read_jsonl
from sklearn.preprocessing import MultiLabelBinarizer
from azure.storage.blob import BlobClient
from typing import Dict, List, Iterable
import numpy as np
from functools import reduce
from nltk.metrics import agreement

blob = BlobClient(
    account_url="https://pkpdaiannotations.blob.core.windows.net",
    container_name="pkpdaiannotations",
    blob_name="tableclass-test-covs-200B-output.jsonl",
    credential="UpC2SPFbEqJdY0tgY91y1oVe3ZcQwxALkJ2QIDTYN17FoTLmpltCFyzxKk13fjrp04y+7K4L6t5KR6VOMUKOqw==")

def convert_labels(inp_labels: List[List[str]]):
    """Transforms labels to vector of binary numbers"""
    mlb = MultiLabelBinarizer(classes=(1, 2, 3, 4, 5, 6))
    all_transformed_labels = mlb.fit_transform(inp_labels)
    all_transformed_labels = list(all_transformed_labels)
    # print(all_transformed_labels[1:4])
    return all_transformed_labels

def sublists_to_dummies(f, sublist, annotator, index_key=None):
    '''Function to convert column containing lists to binary column for each label'''
    categories = [1, 2, 3, 4, 5, 6]
    frame = pd.DataFrame(columns=categories)
    for d, i in f.iterrows():
        if type(i[sublist]) == list or np.array:
            try:
                if index_key != None:
                    key = i[index_key]
                    f = np.zeros(len(categories))
                    for j in i[sublist]:
                        f[categories.index(j)] = 1
                    if key in frame.index:
                        for j in i[sublist]:
                            frame.loc[key][j] += 1
                    else:
                        frame.loc[key] = f
                else:
                    f = np.zeros(len(categories))
                    for j in i[sublist]:
                        f[categories.index(j)] = 1
                    frame.loc[d] = f
            except:
                pass
    ann = annotator.split("-")[4]
    final_frame = frame.add_prefix(str(ann))
    return final_frame


filename = "temp_annotations.jsonl"
with open(filename, "wb") as f:
    f.write(blob.download_blob().readall())

annotations = list(read_jsonl(filename))
uq_annotators = set([x["_session_id"] for x in annotations])

dfs = []
for annotator in uq_annotators:
    sub_annotations = [an for an in annotations if an["_session_id"] == annotator]
    sub_df = pd.DataFrame(sub_annotations)
    dummy_df = sublists_to_dummies(sub_df, "accept", annotator=annotator, index_key="text")
    final_df = dummy_df.reset_index()
    dfs.append(final_df)

df_final = reduce(lambda left, right: pd.merge(left, right, on="index"), dfs)
print(df_final)

a=1

#label 1
data1 = []
for idx, row in df_final.iterrows():
    data1.append(("a1", idx, row["palang1"]))
    #data1.append(("a2", idx, row["gill1"]))
    data1.append(("a3", idx, row["vicky1"]))
    #data1.append(("a4", idx, row["frank1"]))
    #data1.append(("a5", idx, row["pum1"]))

#label 2
data2 = []
for idx, row in df_final.iterrows():
    data2.append(("a1", idx, row["palang2"]))
    #data2.append(("a2", idx, row["gill2"]))
    data2.append(("a3", idx, row["vicky2"]))
    #data2.append(("a4", idx, row["frank2"]))
    #data2.append(("a5", idx, row["pum2"]))

#label 3
data3 = []
for idx, row in df_final.iterrows():
    data3.append(("a1", idx, row["palang3"]))
    #data3.append(("a2", idx, row["gill3"]))
    data3.append(("a3", idx, row["vicky3"]))
    #data3.append(("a4", idx, row["frank3"]))
    #data3.append(("a5", idx, row["pum3"]))

#label 4
data4 = []
for idx, row in df_final.iterrows():
    data4.append(("a1", idx, row["palang4"]))
    #data4.append(("a2", idx, row["gill4"]))
    data4.append(("a3", idx, row["vicky4"]))
    #data4.append(("a4", idx, row["frank4"]))
    #data4.append(("a5", idx, row["pum4"]))

#label 5
data5 = []
for idx, row in df_final.iterrows():
    data5.append(("a1", idx, row["palang5"]))
    #data5.append(("a2", idx, row["gill5"]))
    data5.append(("a3", idx, row["vicky5"]))
    #data5.append(("a4", idx, row["frank5"]))
    #data5.append(("a5", idx, row["pum5"]))


#label 6
data6 = []
for idx, row in df_final.iterrows():
    data6.append(("a1", idx, row["palang6"]))
    #data6.append(("a2", idx, row["pum6"]))
    data6.append(("a3", idx, row["vicky6"]))
    #data6.append(("a4", idx, row["frank6"]))
    #data6.append(("a5", idx, row["gill6"]))


#calculate agreement
label_1 = agreement.AnnotationTask(data=data1)
label_2 = agreement.AnnotationTask(data=data2)
label_3 = agreement.AnnotationTask(data=data3)
label_4 = agreement.AnnotationTask(data=data4)
label_5 = agreement.AnnotationTask(data=data5)
label_6 = agreement.AnnotationTask(data=data6)

#print
print("Cohen's Kappa Label 1:", label_1.kappa())
print("Cohen's Kappa Label 2:", label_2.kappa())
print("Cohen's Kappa Label 3:", label_3.kappa())
print("Cohen's Kappa Label 4:", label_4.kappa())
print("Cohen's Kappa Label 5:", label_5.kappa())
print("Cohen's Kappa Label 6:", label_6.kappa())
print("\n")
print("Fleiss's Kappa Label 1:", label_1.multi_kappa())
print("Fleiss's Kappa Label 2:", label_2.multi_kappa())
print("Fleiss's Kappa Label 3:", label_3.multi_kappa())
print("Fleiss's Kappa Label 4:", label_4.multi_kappa())
print("Fleiss's Kappa Label 5:", label_5.multi_kappa())
print("Fleiss's Kappa Label 6:", label_6.multi_kappa())
a = 1
