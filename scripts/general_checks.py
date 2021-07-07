import jsonlines


with jsonlines.open("../data/json/test_removed/A-BpmctablesNotest.jsonl") as reader:
    json_check = []
    for obj1 in reader:
        json_check.append(obj1)

print(len([i for i in json_check if i]))

