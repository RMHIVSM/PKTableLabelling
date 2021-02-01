# imports
from typing import List
import os
from lxml import etree
from itertools import chain
from io import StringIO
import jsonlines
from tqdm import tqdm


def stringify_children(node):
    """
    Filters and removes possible Nones in texts and tails
    """
    parts = ([node.text] +
             list(chain(*([c.text, c.tail] for c in node.getchildren()))) +
             [node.tail])
    return ''.join(filter(None, parts))


def tables_to_dict(path) -> List:
    """
    Converts tables in xml papers to dictionary
    """

    tree = etree.parse(path)
    root = tree.getroot()
    tables = tree.xpath("//body//sec//table-wrap")
    article_info = tree.xpath("//front//article-meta")

    for info in article_info:
        try:
            pmid = info.find("article-id[@pub-id-type= 'pmc']").text
        except:
            print(info)

    table_dicts = list()
    for table in tables:
        label = table.find('label').text
        caption = stringify_children(table.find('caption'))
        table_xml = etree.tostring(table.find('table'), encoding='unicode')
        # table_xml = table_xml[2:-1]
        table_dict = {'pmid': pmid,
                      'label': label,
                      'caption': caption.strip(),
                      'table': table_xml}
        table_dicts.append(table_dict)

    return table_dicts


def write_html(table_dicts, path):
    """Function to convert the table from XML to HTML for visualization during labelling"""
    for i in table_dicts:
        add_front = "<!DOCTYPE html><html><head><style> table, th, td {border: 1px solid black;}</style></head><body>"
        add_end = "</body></html>"
        xx = str(table_dicts[i]["table"])
        xx = add_front + xx[2:]
        xx = xx[:-1] + add_end
        parser = etree.HTMLParser()
        tree_parsed = etree.parse(StringIO(xx), parser)
        tree_parsed.write(path)


def create_jsonl(table_dicts, json_path):
    """Function to convert XML table dictionary to HTML then to JSONL file for input to prodigy"""

    html_template = "<!DOCTYPE html><html><body><h1>{0}</h1><head><style> table, th, td {{border: 1px solid black;}}</style></head><body>{1}</body></html>"

    html_data = []
    for i in table_dicts:
        html = html_template.format(i["caption"], i["table"])
        text = "Pmid= {}:Table= {}".format(i["pmid"], i["label"])
        html_data.append(dict(html=html, text=text))

    with jsonlines.open(json_path, mode='w') as writer:
        writer.write_all(html_data)


def get_file_list(my_dir):
    """return list of all files from my directory"""
    file_list = []
    for filename in os.listdir(my_dir):
        if filename.endswith(".nxml"):
            file = [os.path.join(my_dir, filename).replace("\\", "/")]
            file_list += file
        else:
            continue

    return file_list


def apply_to_all(file_list):
    """Function to apply tables to dict to all files in file_list"""
    table_list = []
    total_count= 0
    for file in tqdm(file_list):
        try:
            table_dict = tables_to_dict(file)
            if table_dict is not []:
                table_list += table_dict
        except Exception as err:
            pass
            total_count+=1

    print(f"(Total Count= {total_count}")
    return table_list
