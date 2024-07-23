import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress")
label2 = sg.Text("Select destination folder")
in_1 = sg.InputText("")
in_2 = sg.InputText("")

btn1 = sg.FilesBrowse("Choose")
btn2 = sg.FolderBrowse("Choose")
btn3 = sg.Button("Compress")

window = sg.Window("FILE COMPRESSER", [[label1,in_1,btn1], [label2,in_2,btn2],[btn3]])
window.read()
window.close()
