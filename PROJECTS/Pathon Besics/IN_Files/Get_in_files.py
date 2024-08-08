import glob

in_files = glob.glob("D:\My_DOC\data_text\IN_Files\*.txt")

for filepath in in_files:
    with open(filepath, 'r') as file:
        print(file.readlines())

