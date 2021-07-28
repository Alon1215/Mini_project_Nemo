import os, subprocess

nemo = '../NEMO-main/nemo.py'
outputdir = 'output'
os.chdir('../NEMO-main')

with open('../output_handler/desc_reg_only.txt', 'r', encoding='utf8') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        with open(f'input/{i}.txt', 'w', encoding='utf8') as tmp:
            tmp.write(line)

        filename = f'{i}.txt'
        # output_file_path = outputdir + '\\' + filename + ".txt"
        output_file_path = f'{outputdir}/{i}.txt'

        # command = ['python',
        #            nemo,
        #            'run_ner_model',
        #            'token-single',
        #            filename,
        #            output_file_path]

        # subprocess.call(command)
        os.system(f"python nemo.py run_ner_model token-single input/{i}.txt output/{i}.txt")
        os.remove(f'input/{i}.txt')
        print(i)


