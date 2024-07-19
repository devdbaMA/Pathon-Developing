file_path = "D:\My_DOC\data_text"
file_name = input("Enter file name" + "\n")

with open(f"{file_path}\{file_name}.txt", "w" ) as file:
    file = file.write(file_name)