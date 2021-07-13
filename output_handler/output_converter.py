import time
import itertools as it
import pandas
import numpy as np


def demo_convert_titles_to_txt():
    # path_input = 'C:\Users\User\Downloads\Mini_project_Nemo\NEMO-main\example.txt'
    # path_csv = 'new_csv'
    # path_csv = "C:\Users\User\Downloads\json.metadata.sys.final.csv"
    path_csv = '../../json.metadata.sys.final.csv'

    # writing to file
    df = pandas.read_csv(path_csv)
    arr = df['archiveName'].tolist()

    # ent_str = [', '.join(str(s)) for s in arr]
    # np.savetxt(r'text_try.txt', ent_str)
    # with open(f'{path_input}.txt', 'w') as f:
    file1 = open("file1.txt", 'w')
    file1.writelines(arr)
    file1.close()


filename = '../NEMO-main/final_output3.txt'


def create_csv_entities_only(name, total_entities_dict):
    # Create new csv file with entities
    df = pandas.DataFrame()
    for key, value in total_entities_dict:
        df[key] = value
    df.to_csv(f'{name}_entities_only.csv')


def create_csv_entities_and_data(name, csv_path, total_entities_dict):
    # Add new column to data file
    df = pandas.read_csv(csv_path)
    for key, value in total_entities_dict:
        df[key] = value
    df.to_csv(f'{name}_all.csv')


def create_csv_title_desc_entities(name, csv_path, total_entities_dict):
    archive = pandas.read_csv(csv_path)
    output = pandas.DataFrame()
    # output['archiveName'] = archive['archiveName']
    # output['entities'] = total_entities_list
    output['Title'] = archive['displayValue']
    for key, value in total_entities_dict.items():
        output[key] = value

    output.to_csv(f'{name}_mini.csv')


def analyze_and_generate_output():
    with open(filename, 'r') as f:
        # total_entities_list = []
        total_entities_dict = {"ORG": [], "GPE": [], "PER": [], "LOC": [], "FAC": [], "EVE": [], "ANG": [], "WOA": [],
                               "DUC": []}
        content_list = f.read().split('# 1.0000')
        for block in content_list:
            if len(block.strip()) > 0:
                # entities_list = []
                entities_dict = {"ORG": [], "GPE": [], "PER": [], "LOC": [], "FAC": [], "EVE": [], "ANG": [], "WOA": [],
                               "DUC": []}
                lines = block.split('\n')
                entity = ''
                for line in lines:
                    word_token = line.split(" ")
                    if len(word_token) == 2 and word_token[1] != 'O':
                        # entity = entity + word_token[0] + " "
                        entity = " ".join([entity, word_token[0]])
                        token_parsed = word_token[1].split("-")
                        if token_parsed[0] == 'E' or token_parsed[0] == 'S':
                            # entity = entity.strip()
                            # entities_list.append(entity)
                            try:
                                entities_dict[token_parsed[1]].append(entity)
                            except KeyError:
                                entities_dict[token_parsed[1]] = [entity]

                            entity = ''  # reset entity aggregation

                # update every NER entity recognized by Nemo
                for key in entities_dict.keys():
                    try:
                        total_entities_dict[key].append(entities_dict[key])
                    except KeyError:
                        total_entities_dict[key] = [entities_dict[key]]

                # total_entities_list.append(entities_list)
                # print('block entities: {}'.format(entities_list))
                # print("-------------\nFINISHED BLOCK\n-------------\n")
        # print(total_entities)
        create_csv_title_desc_entities('result', '../../json.metadata.sys.final.csv', total_entities_dict)


analyze_and_generate_output()
