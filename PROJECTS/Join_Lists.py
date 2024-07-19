file_path = "D:\My_DOC\data_text"

contetns = ["first my project in pathon ","second kod thitch I made","sird kod is fun"]

files = ["first_kod.txt","second_kod.txt","sird_kod.txt"]

for contect, file in zip(contetns,files):
    with open(f"{file_path}\{file}", "w") as fd:
         fd = fd.write(contect)








