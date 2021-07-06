#imports
import jsonlines
import random
#from pk_tables.xml_preprocessing import split_data

############
#split_data("../data/json/pmctables.jsonl", "../data/json/")


with jsonlines.open("../data/json/train_1500.jsonl") as reader:
        json_list = []
        for obj in reader:
            json_list.append(obj)

        random.Random(4).shuffle(json_list)
        train_1000to1250 = json_list[:250]
        train_1250to1500 = json_list[250:500]

        with jsonlines.open("../data/json/" + "train_1000to1250.jsonl", mode='w') as writer:
            writer.write_all(train_1000to1250)

        with jsonlines.open("../data/json/" + "train_1250to1500.jsonl", mode='w') as writer:
            writer.write_all(train_1250to1500)




