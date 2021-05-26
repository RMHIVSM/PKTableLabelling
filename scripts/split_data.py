#imports
import jsonlines
import random
#from pk_tables.xml_preprocessing import split_data

############
#split_data("../data/json/pmctables.jsonl", "../data/json/")


with jsonlines.open("../data/json/train_tableclass.jsonl") as reader:
        json_list = []
        for obj in reader:
            json_list.append(obj)

        random.Random(4).shuffle(json_list)
        train_500 = json_list[:500]
        train_1000 = json_list[500:1000]
        train_1500 = json_list[1000:1500]
        train_2000 = json_list[1500:2000]

        with jsonlines.open("../data/json/" + "train_500.jsonl", mode='w') as writer:
            writer.write_all(train_500)

        with jsonlines.open("../data/json/" + "train_1000.jsonl", mode='w') as writer:
            writer.write_all(train_1000)

        with jsonlines.open("../data/json/" + "train_1500.jsonl", mode='w') as writer:
            writer.write_all(train_1500)

        with jsonlines.open("../data/json/" + "train_2000.jsonl", mode='w') as writer:
            writer.write_all(train_2000)

