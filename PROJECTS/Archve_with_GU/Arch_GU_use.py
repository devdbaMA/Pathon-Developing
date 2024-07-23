import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress")
label2 = sg.Text("Select destination folder")
in_1 = sg.InputText("")
in_2 = sg.InputText("")

btn1 = sg.FilesBrowse("Choose", key="files")
btn2 = sg.FolderBrowse("Choose", key="folder")
btn3 = sg.Button("Compress")

layout = [
    [label1, in_1, btn1],
    [label2, in_2, btn2],
    [btn3]
]

window = sg.Window("FILE COMPRESSER", layout)

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Compress":
        filepath = value['files'].split(';')
        folder = value['folder']
        print("Files to compress:", filepath)
        print("Destination folder:", folder)

window.close()
