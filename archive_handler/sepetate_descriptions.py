import time
import itertools as it
import pandas
import numpy as np
import re

def generate_description_files():
    path_csv = '../../json.metadata.sys.final.csv'

    # writing to file
    df = pandas.read_csv(path_csv)
    df['combined'] = df['_objectDescription_objectDesc_displayValue'].fillna('none').astype(str)
    arr = df['combined'].tolist()


    for i, line in enumerate(arr):
        with open(f"desc/{i}.txt", 'w', encoding='utf8') as file:
            words = re.sub(r'\W+[^\u0590-\u05FF\u200f\u200e ]+', '', line).split()
            cleaned_sentenced = " ".join(words)
            file.writelines(cleaned_sentenced)

if __name__ == "__main__":
    generate_description_files()
