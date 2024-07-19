import os
file_path = 'D:\\My_DOC\\data_text\\list_info.txt'

def get_dat():
    """Read data in text file"""
    with open(file_path, 'r') as file_in:
        return file_in.readlines()

def get_dat_n():
    """Read data in text file and print with indexes"""
    with open(file_path, 'r') as file_in:
        dat = file_in.readlines()
        for index, line in enumerate(dat):
            print(f"Row {index}: {line.strip()}")
    return dat

def put_dat(dat):
    """Write data in text file"""
    with open(file_path, "w") as file:
        file.writelines(dat)