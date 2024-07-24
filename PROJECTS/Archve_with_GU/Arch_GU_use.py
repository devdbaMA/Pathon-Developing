import FreeSimpleGUI as sg
import zipfile
import os

label1 = sg.Text("Select files to compress")
label2 = sg.Text("Select destination folder")
label3 = sg.Text("Enter name for compressed file (without extension)")

in_files = sg.InputText("")
in_folder = sg.InputText("")
in_filename = sg.InputText("", size=(32, 1))

btn_files = sg.FilesBrowse("Choose", key="files")
btn_folder = sg.FolderBrowse("Choose", key="folder")
btn_compress = sg.Button("Compress")

layout = [
    [label1, in_files, btn_files],
    [label2, in_folder, btn_folder],
    [label3, in_filename],
    [btn_compress]
]

window = sg.Window("FILE COMPRESSER", layout)

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Compress":
        filepaths = value['files'].split(';')
        folder = value['folder']
        zip_filename = value[2].strip()  # Input text index for filename is 2

        if not filepaths or not folder or not zip_filename:
            sg.popup("Please select files, a destination folder, and enter a file name.")
            continue

        zip_filepath = os.path.join(folder, f"{zip_filename}.zip")

        with zipfile.ZipFile(zip_filepath, 'w') as zipf:
            for filepath in filepaths:
                zipf.write(filepath, os.path.basename(filepath))

        sg.popup("Files compressed successfully!")

window.close()
