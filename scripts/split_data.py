#imports
import jsonlines
#from pk_tables.xml_preprocessing import split_data

############
#split_data("../data/json/pmctables.jsonl", "../data/json/")


with jsonlines.open("../data/json/testjson.jsonl") as reader:
        json_list = []
        for obj in reader:
            json_list.append(obj)

        test_100 = json_list[:100]
        test_900 = json_list[100:]

        with jsonlines.open("../data/json/" + "test_100.jsonl", mode='w') as writer:
            writer.write_all(test_100)

        with jsonlines.open("../data/json/" + "test_900.jsonl", mode='w') as writer:
            writer.write_all(test_900)
