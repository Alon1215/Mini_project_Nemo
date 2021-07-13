import time
import itertools as it
import pandas
import numpy as np

#
# with open('file1.txt', 'r', encoding='utf8') as f:
#     print(f.read())


def convert_documents_to_nemo_input(output_name):
    # path_input = 'C:\Users\User\Downloads\Mini_project_Nemo\NEMO-main\example.txt'
    # path_csv = 'new_csv'
    # path_csv = "C:\Users\User\Downloads\json.metadata.sys.final.csv"
    path_csv = '../../json.metadata.sys.final.csv'

    # writing to file
    df = pandas.read_csv(path_csv)
    # arr = list(df['archiveName'])
    # titles = df['displayValue']
    # df['combined'] = df['_objectDescription_objectDesc_displayValue'].fillna('')
    df['combined'] = df[['displayValue', '_objectDescription_objectDesc_displayValue']].fillna('').agg('. '.join, axis=1)
    arr = list(df['combined'])

    print(len(arr))
    # with open(f'{path_input}.txt', 'w') as f:
    with open(f"{output_name}.txt", 'w', encoding='utf8') as file:
        # arr_str = '\n'.join(str(s).replace("\n", '') for s in arr)
        arr_str = '\n'.join(" ".join(str(s).split()) for s in arr)
        print(arr_str.count("\n"))
        file.writelines(arr_str)
        # for line in arr:
        #     file.write(line)
        #     file.write('\n')


convert_documents_to_nemo_input("title_desc3")
