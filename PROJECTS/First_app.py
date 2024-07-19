#------------- ENV VARABLES-------------------------
j = 0
dat = []
file_info = []
import os
file_path = 'D:\My_DOC\data_text\list_info.txt'
#----------------------------------------------------

def get_dat():
    """Read data in text file"""
    with open(file_path, 'r') as file_in:
        dat = file_in.readlines()
    return dat


def get_dat_n():
    """ Read data in text file and print with indexes"""
    with open(file_path, 'r') as file_in:
        for index, line in enumerate(file_in):
            print(f"Row {index}: {line.strip()}")
    return index,line


def put_dat():
    """Write data in text file"""
    with open(file_path, "w") as file:
        file.writelines(dat)


while True:
    print("")
    st_in = input("Input (I) Edit(E) Delete(D)  print (P) Quit(Q): ")
    match st_in:
#----------------------------------------------------------------------
        case "I": # / INSERT OPARATION /
            in_data = input("Enter the Value: ") + "\n"
            if os.path.exists(file_path):
                dat = get_dat()
                dat.append(in_data)
                dat = put_dat()
            else:
                dat.append(in_data)
                put_dat(dat)

#-----------------------------------------------------------------
        case "E": # / UPDATE OPARATION /
            if os.path.exists(file_path):
                dat = get_dat_n()
                d = int(input("Enter number of deleted rows"))

                dat = get_dat()
                if 0 <= d < len(dat):
                    up_dat = input("Enter new value")+ "\n"
                    dat[d] = up_dat
                    dat = put_dat()
                    dat = get_dat_n()
                else:
                    print("Invalid row number")

                    dat = get_dat_n()
            else:
                print("the file does not exist")
#----------------------------------------------------------------
        case "P": # / SHOW OPARATION /
            def file_loc(file_path):
                try:
                    dat = get_dat_n()
                except FileNotFoundError:
                    print("the file does not exist")
                    return None
            file_loc(file_path)
#-----------------------------------------------------------------
        case "D": # / DELETE OPARATION /
            if os.path.exists(file_path):
                dat = get_dat_n()

                d = int(input("Enter number of deleted rows"))
                dat = get_dat()
                if 0 <= d < len(dat):
                    dat.pop(d)
                    dat = put_dat()
                    dat= get_dat_n()
                else:
                    print("Invalid row number")

                    dat = get_dat_n()
            else:
                print("the file does not exist")
#-------------------------------------------------------------------
        case "Q": # / EXIT OPARATION /
            break
        case _:
            print("Invalid option, please enter I E D P Q")





