#imports
import jsonlines
import random
#from pk_tables.xml_preprocessing import split_data

############
#split_data("../data/json/pmctables.jsonl", "../data/json/")


with jsonlines.open("../data/json/test_900.jsonl") as reader:
        json_list = []
        for obj in reader:
            json_list.append(obj)

        random.Random(4).shuffle(json_list)
        test_250A = json_list[:250]
        test_250B = json_list[250:500]
        test_remaining_400 = json_list[500:901]


        with jsonlines.open("../data/json/" + "test_250A.jsonl", mode='w') as writer:
            writer.write_all(test_250A)

        with jsonlines.open("../data/json/" + "test_250B.jsonl", mode='w') as writer:
            writer.write_all(test_250B)

        with jsonlines.open("../data/json/" + "test_remaining_400.jsonl", mode='w') as writer:
            writer.write_all(test_remaining_400)
