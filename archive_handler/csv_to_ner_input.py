import pandas
import re


def convert_documents_to_nemo_input(titles_name, descriptions_name, path_csv='../../json.metadata.sys.final.csv'):
    """
    Main method of converting the data from csv to Nemo input file,
    It extract the titles & descriptions from input csv,
    and create_nemo_input(...) for each one.

    :param titles_name: name of titles output file
    :param descriptions_name: name of descriptions output file
    :param path_csv: path to input csv file
    """
    # writing to file
    df = pandas.read_csv(path_csv)

    # titles case:
    df['displayValue'] = df['displayValue'].fillna('none').astype(str)
    # descriptions case:
    df['objectDescription'] = df['_objectDescription_objectDesc_displayValue'].fillna('none').astype(str)


    arr_input = df['displayValue'].tolist()
    create_nemo_input(arr_input, titles_name)

    arr_input = df['objectDescription'].tolist()
    create_nemo_input(arr_input, descriptions_name)


def create_nemo_input(arr_input, output_name):
    """
    Create Nemo input, and place it in input folder for Nemo processing.
    1. clean and replace bad characters in input csv.
    2. discard records with an empty cell (for example: not every document has a description).
    3. mark each line with the index of it's document.
    4, create a file consist of each line for each document.

    :param arr_input: column from the csv converted to a list
    :param output_name: "titles.txt" OR "description.txt"
    """
    with open(f"input/{output_name}", 'w', encoding='utf8') as file:

        counter = 0
        for i in range(len(arr_input)):
            if i % 10000 == 0:
                print(i)  # DEBUG
            line = arr_input[i]

            if line != "none":
                line = re.sub(r"[\n\t\v\b\r\f\a]", " ", line)
                line_cleaned = f"{i}: " + " ".join(
                    re.sub(r'[^a-zA-Z0-9\u0590-\u05FF\u200f\u200e ,".]', " ", line).split())
                file.writelines(line_cleaned)
                file.write('\n\n')
            else:
                counter += 1
        print(f"blank descriptions = {counter}")


if __name__ == "__main__":
    convert_documents_to_nemo_input("titles.txt", "description.txt")



