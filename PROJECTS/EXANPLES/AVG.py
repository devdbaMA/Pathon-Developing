#------------- ENV VARABLES-------------------------
file_path = 'D:\My_DOC\data_text\list_info.txt'

def get_dat():
    with open(file_path, 'r') as file_in:
        dat = file_in.readlines()

    values = dat[1:]
    lst_values = [float(i) for i in values]
    avg_values = sum(lst_values)/len(lst_values)
    return avg_values

print(f" AVG Values is {get_dat()}")

