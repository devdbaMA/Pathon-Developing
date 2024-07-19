from PROJECTS.Impruve_First_project.Functions import get_dat, get_dat_n, put_dat
import time
import os

file_path = 'D:\\My_DOC\\data_text\\list_info.txt'

now = time.strftime("%d.%m.%Y %H:%M:%S")

while True:
    print(" ")
    print(now)
    st_in = input("Input (I) Edit(E) Delete(D)  print (P) Quit(Q): ")
    match st_in:
        case "I":  # INSERT OPERATION
            in_data = input("Enter the Value: ") + "\n"
            if os.path.exists(file_path):
                dat = get_dat()
            else:
                dat = []
            dat.append(in_data)
            put_dat(dat)

        case "E":  # UPDATE OPERATION
            if os.path.exists(file_path):
                dat = get_dat_n()
                d = int(input("Enter number of the row to be updated: "))
                if 0 <= d < len(dat):
                    up_dat = input("Enter new value: ") + "\n"
                    dat[d] = up_dat
                    put_dat(dat)
                else:
                    print("Invalid row number")
            else:
                print("The file does not exist")

        case "P":  # SHOW OPERATION
            if os.path.exists(file_path):
                get_dat_n()
            else:
                print("The file does not exist")

        case "D":  # DELETE OPERATION
            if os.path.exists(file_path):
                dat = get_dat()
                d = int(input("Enter number of the row to be deleted: "))
                if 0 <= d < len(dat):
                    dat.pop(d)
                    put_dat(dat)
                else:
                    print("Invalid row number")
            else:
                print("The file does not exist")

        case "Q":  # EXIT OPERATION
            break

        case _:
            print("Invalid option, please enter I E D P Q")