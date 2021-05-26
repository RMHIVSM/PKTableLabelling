import jsonlines

with jsonlines.open("../data/json/all_pmcs/A-Bpmctables.jsonl") as reader1:
    json_check = []
    for obj1 in reader1:
        json_check.append(obj1)

with jsonlines.open("../data/json/test_tableclass.jsonl") as reader2:
    json_base = []
    for obj2 in reader2:
        json_base.append(obj2)

for i in json_check:
    final_json = []
    if i not in json_base:
        final_json.append(i)

with jsonlines.open("../data/json/test_removed/checkcheck.jsonl", mode='w') as writer:
    writer.write_all(final_json)

