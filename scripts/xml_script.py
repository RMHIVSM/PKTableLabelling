#imports
import jsonlines
from pk_tables.xml_preprocessing import file_list_folders, apply_to_all, create_jsonl,
#########

file_list = file_list_folders('../data/xml/Untarred_files/O-Z')

table_list = apply_to_all(file_list)

create_jsonl(table_list, '../data/json/O-Zpmctables.jsonl')

