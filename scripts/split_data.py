#imports
import jsonlines
import random
#from pk_tables.xml_preprocessing import split_data

############
#split_data("../data/json/pmctables.jsonl", "../data/json/")


with jsonlines.open("../data/final-out-concat/final_data/final-out-test1000.jsonl") as reader:
        json_list = []
        for obj in reader:
            json_list.append(obj)

        random.Random(4).shuffle(json_list)
        builder_test100 = json_list[:100]
        builder_val100 = json_list[100:200]
        builder_train800 = json_list[200:1000]

        with jsonlines.open("../data/final-out-concat/" + "builder_test100.jsonl", mode='w') as writer:
            writer.write_all(builder_test100)

        with jsonlines.open("../data/final-out-concat/" + "builder_val100.jsonl", mode='w') as writer:
            writer.write_all(builder_val100)

        with jsonlines.open("../data/final-out-concat/" + "builder_train800.jsonl", mode='w') as writer:
            writer.write_all(builder_train800)



