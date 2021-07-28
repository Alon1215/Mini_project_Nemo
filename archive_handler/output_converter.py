import time
import itertools as it
import pandas
import numpy as np

def create_csv_entities_only(name, total_entities_dict):
    """
    Create csv file with the obtained entities only
    :param name: name of csv file
    :param total_entities_dict: obtained entities
    """
    # Create new csv file with entities
    df = pandas.DataFrame()
    for key, value in total_entities_dict:
        df[key] = value
    df.to_csv(f'{name}_entities_only.csv')


def create_csv_entities_and_data(name, csv_path, total_entities_dict):
    """
    Append obtained entities to the original data
    :param name: name of csv file to output
    :param csv_path: path to data cdv
    :param total_entities_dict: obtained entities
    :return: new file with the data + entities
    """
    # Add new column to data file
    df = pandas.read_csv(csv_path)
    for key, value in total_entities_dict:
        df[key] = value
    df.to_csv(f'{name}_all.csv')


def create_csv_title_desc_entities(name, csv_path, total_entities_list):
    """
    Create csv file similar to "create_csv_entities_only(...)",
    but connect between a document to entities based on index in the begining of the parsed Nemo output.
    Caompatible with phase 2 of the project.
    :param csv_path: path to data cdv
    :param total_entities_dict: obtained entities
    :return: new file with the data + entities
    """
    output = pandas.DataFrame()

    entities_dict = {"ORG": [], "GPE": [], "PER": [], "LOC": [], "FAC": [], "EVE": [], "ANG": [], "WOA": [],
                     "DUC": []}

    for document_dict in total_entities_list:
        for key in document_dict:
            entities_dict[key].append(document_dict[key])

    for key, value in entities_dict.items():
        # convert each document-category entities to string joined by comma
        output[key] = [", ".join(words) for words in value]

    output.to_csv(f'{name}_mini.csv')


def analyze_and_generate_output(filename,outputname):
    """
    Main method of converting Nemo output to csv file.
    Parse output of every document, extract entities based on Nemo paper and entities tags,
    Create a list, for each document a dictionary with entities per category.
    In the end calls to one of the 3 methods to create the output csv

    :param filename: Nemo output file to process
    :param outputname: csv name (output)
    """
    with open(filename, 'r') as f:
        total_entities_list = [{"ORG": [], "GPE": [], "PER": [], "LOC": [], "FAC": [], "EVE": [], "ANG": [], "WOA": [],
                                "DUC": []} for i in range(385334)]
        content_list = f.read().split('# 1.0000')
        count = 0
        for block in content_list:
            if len(block.strip()) > 0:
                document_number = -1  # Index in csv file
                lines = block.split('\n')
                entity = ''
                for index, line in enumerate(lines):
                    word_token = line.split(" ")

                    # Extract document's index:
                    if document_number == -1 and word_token[0].isnumeric():
                        document_number = int(word_token[0])  # extract index of result
                    else:
                        if len(word_token) == 2 and word_token[1] != 'O':
                            entity = " ".join([entity, word_token[0]])
                            token_parsed = word_token[1].split("-")
                            if token_parsed[0] == 'E' or token_parsed[0] == 'S':
                                try:
                                    total_entities_list[document_number][token_parsed[1]].append(entity)
                                except KeyError:
                                    total_entities_list[document_number][token_parsed[1]] = [entity]

                                entity = ''  # reset entity aggregation

            else:
                count += 1
        # print(total_entities)
        print(count)
        create_csv_title_desc_entities(outputname, '../../json.metadata.sys.final.csv', total_entities_list)


def combine_entities(title_entities, descriptions_entities):
    if title_entities == "":
        return descriptions_entities
    elif descriptions_entities == "":
        return title_entities
    else:
        return title_entities + ", " + descriptions_entities


def merge_results(titles_path, descriptions_path, data_path):
    entities_dictionary = {"ORG": [], "GPE": [], "PER": [], "LOC": [], "FAC": [], "EVE": [], "ANG": [], "WOA": [],
                           "DUC": []}

    # open 3 files: original data, and 2 results (as csv files)
    titles_csv = pandas.read_csv(titles_path).fillna("").astype(str)
    descriptions_csv = pandas.read_csv(descriptions_path).fillna("").astype(str)
    data_csv = pandas.read_csv(data_path)
    output_csv = pandas.DataFrame()
    output_csv['displayValue'] = data_csv['displayValue']
    output_csv['objectDescription'] = data_csv['_objectDescription_objectDesc_displayValue'].fillna('').astype(str)

    # Aggregate results of both titles & descriptions:
    for key in entities_dictionary.keys():
        for title_entities, descriptions_entities in zip(titles_csv[key].tolist(), descriptions_csv[key].tolist()):
            entities_dictionary[key].append(combine_entities(title_entities, descriptions_entities))

    # Append results to data and finish process:
    for key, value in entities_dictionary.items():
        data_csv[key] = value
        output_csv[key] = value

    data_csv.to_csv('output/metadata_final.csv')
    output_csv.to_csv('output/output_final.csv')


if __name__ == "__main__":
    analyze_and_generate_output('output/titles.txt', 'output/result_titles')
    analyze_and_generate_output('output/descriptions.txt', 'output/result_descriptions')
    merge_results('output/result_titles_mini.csv', 'output/result_descriptions_mini.csv', '../../json.metadata.sys.final.csv')
