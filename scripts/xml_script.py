#imports
from pk_tables.xml_preprocessing import get_file_list, apply_to_all, create_jsonl, tables_to_dict
#########

file_list = get_file_list('../data/xmls/selected_pmc/')

table_list= apply_to_all(file_list)

create_jsonl(table_list, '../data/json/pmctables_json.jsonl')

