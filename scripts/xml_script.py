#imports
from pk_tables.concat_parwithcovs import concat_parwithcovs, concat_lists, labels_update
#########

#file_list = file_list_folders('../data/xml/Untarred_files/O-Z')

#table_list = apply_to_all(file_list)

#create_jsonl(table_list, '../data/json/all_pmcs/O-Zpmctables.jsonl')


concat_parwithcovs("../data/final-out/test/final-out-pars-test1000.jsonl",
                   "../data/final-out/test/final-out-covs-test1000.jsonl",
                   "final-out-test1000.jsonl",
                   check_text= "3")

