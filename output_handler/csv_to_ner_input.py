import time
import itertools as it
import pandas
import numpy as np

with open('file1.txt', 'r', encoding='utf8') as f:
    print(f.read())


def convert_titles_to_txt():
    # path_input = 'C:\Users\User\Downloads\Mini_project_Nemo\NEMO-main\example.txt'
    # path_csv = 'new_csv'
    # path_csv = "C:\Users\User\Downloads\json.metadata.sys.final.csv"
    path_csv = '../../json.metadata.sys.final.csv'

    # writing to file
    df = pandas.read_csv(path_csv)
    arr = list(df['archiveName'])

    # with open(f'{path_input}.txt', 'w') as f:
    file1 = open("file1.txt", 'w', encoding='utf8')
    arr_str = '\n'.join(str(s) for s in arr)
    file1.writelines(arr_str)
    file1.close()
