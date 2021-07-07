import jsonlines
import os

def concat_jsonl(in_file_dir: str, out_file_name: str):

    all_files_list = []
    for filename in os.listdir(in_file_dir):
            with jsonlines.open(os.path.join(in_file_dir, filename)) as reader:
                json_list = []
                for obj1 in reader:
                    json_list.append(obj1)
                    all_files_list.extend(json_list)

    json_uniques = list({x['text']:x for x in all_files_list}.values())

    print(len(json_uniques))

    with jsonlines.open("../data/final-out/test/" + out_file_name, mode='w') as writer:
        writer.write_all(json_uniques)

concat_jsonl("../data/final-out/covs_test/", "final-out-covs-test1000.jsonl")
concat_jsonl("../data/final-out/pars_test/", "final-out-pars-test1000.jsonl")


