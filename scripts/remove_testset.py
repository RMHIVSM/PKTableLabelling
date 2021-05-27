import jsonlines

def remove_testset(check_file, out_file):
    with jsonlines.open(check_file) as reader:
        json_check = []
        for obj1 in reader:
            json_check.append(obj1)

    with jsonlines.open("../data/json/test_tableclass.jsonl") as reader:
        json_base = []
        for obj2 in reader:
            json_base.append(obj2)

    with jsonlines.open("../data/json/test_100.jsonl") as reader:
        for obj3 in reader:
            json_base.append(obj3)

    a_key = "text"
    base_values = [a_dict[a_key] for a_dict in json_base]
    json_keep = [i for i in json_check if i['text'] not in base_values]
    json_uniques = list({x['text']:x for x in json_keep}.values())

    print(len([i for i in json_uniques if i]))

    '''
    check_values = [a_dict[a_key] for a_dict in json_check]
    values_to_keep = list(set(check_values)- set(base_values))
    print(len(base_values))
    print(len(check_values))
    print(len(set(values_to_keep)))
    print(len(json_uniques))
    print(json_uniques[1])
    '''

    with jsonlines.open(out_file, mode='w') as writer:
        writer.write_all(json_uniques)

remove_testset("../data/json/all_pmcs/A-Bpmctables.jsonl", "../data/json/test_removed/A-BpmctablesNotest.jsonl")
remove_testset("../data/json/all_pmcs/C-Hpmctables.jsonl", "../data/json/test_removed/C-HpmctablesNotest.jsonl")
remove_testset("../data/json/all_pmcs/I-Npmctables.jsonl", "../data/json/test_removed/I-NpmctablesNotest.jsonl")
remove_testset("../data/json/all_pmcs/O-Zpmctables.jsonl", "../data/json/test_removed/O-ZpmctablesNotest.jsonl")
