import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from skmultilearn.model_selection import IterativeStratification
import jsonlines

with jsonlines.open("../data/final-out-concat/test/final-out-test1000.jsonl") as reader:
    json_list = []
    for obj in reader:
        json_list.append(obj)

mlb = MultiLabelBinarizer()
df = pd.DataFrame(json_list, columns=["text", "accept"])
X = df["text"].to_numpy()
y = mlb.fit_transform(df["accept"])
print(X.shape, type(X))
print(y.shape, type(y))


def iterative_train_test_split(X, y, test_size):
    stratifier = IterativeStratification(n_splits=2, order=2, sample_distribution_per_fold=[test_size, 1.0 - test_size])
    train_indexes, test_indexes = next(stratifier.split(X, y))
    X_train = X[train_indexes]
    X_test = X[test_indexes]
    return X_train, X_test

test_text, val_text = iterative_train_test_split(X, y, test_size=0.33)

print(val_text[1], val_text.shape)
print(test_text[1], test_text.shape)
val_list = list(val_text)
test_list = list(test_text)

val_set = [i for i in json_list if i['text'] not in val_list]
test_set = [i for i in json_list if i['text'] not in test_list]
print(len([i for i in val_set if i]), val_set[3])
print(len([i for i in test_set if i]), test_set[3])

with jsonlines.open("../data/final-out-concat/test_split/" + "val_set333.jsonl", mode='w') as writer:
    writer.write_all(val_set)

with jsonlines.open("../data/final-out-concat/test_split/" + "test_set666.jsonl", mode='w') as writer:
    writer.write_all(test_set)
