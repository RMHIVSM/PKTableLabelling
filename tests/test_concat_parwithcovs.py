#imports
from pk_tables.concat_parwithcovs import remove_notrel

covs_list = [{"text": 1, "accept": [1, 2]}, {"text": 2, "accept": [3, 4]}, {"text": 3, "accept": [5, 6]}]
params_list = [{"text": 1, "accept": [1, 2]}, {"text": 2, "accept": [3, 4]}, {"text": 3, "accept": [5]}]

test= remove_notrel(covs_list)
print(test)

def test_concat_parwithcovs():
    params_file= "../data/final-out/final-test-params100.jsonl"
    covs_file= "../data/final-out/final-test-covs100.jsonl"

    covs_list = [{"text": 1, "accept": [1, 2]}, {"text": 2,"accept": [3, 4]}, {"text": 3, "accept": [5, 6]}]
    params_list = [{"text": 1,"accept": [1, 2]}, {"text": 2,"accept": [3, 4]}, {"text": 3, "accept": [5]}]

    for item in new_json_list:
        if item["text"] ==1:
            assert item["accept"] == [1,2,6,7]


    for item in new_json_list:
        if item["text"] ==2:
            assert item["accept"] == [3,4,8,9]

    for item in new_json_list:
        if item["text"] ==3:
            assert item["accept"] == [10]
