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

filename = '../NEMO-main/example_output5.txt'

with open(filename, 'r') as f:
    total_entities = []
    content_list = f.read().split('# 1.0000')
    for block in content_list:
        if len(block.strip()) > 0:
            entities = []
            lines = block.split('\n')
            entity = ''
            for line in lines:
                arr = line.split(" ")
                if len(arr) == 2 and arr[1] != 'O':
                    entity = entity + arr[0] + " "
                    if arr[1].startswith('E') or arr[1].startswith('S'):
                        entity = entity.strip()
                        entities.append(entity)
                        entity = ''
            total_entities.append(entities)
            # print('block entities: {}'.format(entities))
            # print("-------------\nFINISHED BLOCK\n-------------\n")
    # print(total_entities)

    #
    # # Create new csv file with entities
    # df = pandas.DataFrame()
    # df['entities'] = total_entities
    # df.to_csv('new_csv')

    # # Add new column to data file
    # df = pandas.read_csv('../../json.metadata.sys.final.csv')
    # df['entities'] = total_entities
    # df.to_csv('output.csv'.format(time.time()))

    archive = pandas.read_csv('../../json.metadata.sys.final.csv')
    output = pandas.DataFrame()
    output['archiveName'] = archive['archiveName']
    output['entities'] = total_entities

    output.to_csv('output_min.csv')
