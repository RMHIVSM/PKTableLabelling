#imports
from pk_tables.xml_preprocessing import file_list_folders, apply_to_all, create_jsonl
from pk_tables.concat_parwithcovs import concat_parwithcovs
#########

#file_list = file_list_folders('../data/xml/Untarred_files/O-Z')

#table_list = apply_to_all(file_list)

#create_jsonl(table_list, '../data/json/all_pmcs/O-Zpmctables.jsonl')


concat_parwithcovs("../data/final-out/test/final-test-covs250B.jsonl",
                   "../data/final-out/test/final-test-params250B.jsonl",
                   "final-test-concat-250B.jsonl",
                   check_text= "Pmid= 2405815:Table= Table 2")
