import FreeSimpleGUI as sg
from PROJECTS.Impruve_First_project.With_Interface.Functions import get_dat_n, put_dat
import time
import os

file_path = 'D:\\My_DOC\\data_text\\list_info.txt'
sg.theme("Yellow")

# Define the layout of the window
layout = [
    [sg.Text('', key='-TIME-', font=('Helvetica', 10))],
    [sg.Text("Input data")],
    [sg.InputText(key='input_data'),
     sg.Button("ADD", size=(8,1)),],
    [sg.Listbox(values=[], size=(54, 10), key='listbox')],
     [sg.Button("EDIT", size=(12, 1)),
     sg.Button("SHOW", size=(12, 1)),
     sg.Button("DELETE", key="DELETE", size=(12, 1)),
     sg.Button("CLOSE", size=(12, 1))]
]
# Create the window
window = sg.Window('CRUD Projects', layout, font=('Helvetica', 12), finalize=True)

while True:
    now = time.strftime("%d.%m.%Y %H:%M:%S")
    event, values = window.read(timeout=1000)
    window["-TIME-"].update(now)

    match event:
        case "ADD":  # INSERT OPERATION
            try:
                in_data = values['input_data'] + "\n"
                if os.path.exists(file_path):
                    dat = get_dat_n()
                else:
                    dat = []
                dat.append(in_data)
                put_dat(dat)
                window['input_data'].update([])
                dat = get_dat_n()
                window['listbox'].update(dat)
            except indexError:
                sg.popup("Enter the data")

        case "SHOW":  # INSERT OPERATION
            if os.path.exists(file_path):
                dat = get_dat_n()
                window['listbox'].update(dat)
            else:
                window['listbox'].update([])

        case "DELETE":  # DELETE DATA FROM LIST
            try:
                selected_item = values['listbox']
                if selected_item:
                    dat = get_dat_n()
                    dat.remove(selected_item[0])
                    put_dat(dat)
                    window['listbox'].update([])
                    dat = get_dat_n()
                    window['listbox'].update(dat)
            except ValueError:
                sg.popup("Select row for deteed")

        case "EDIT": # EDITING DATA FROM LIST
            selected_item = values['listbox']
            new_value = values['input_data']+ "\n"
            if selected_item and new_value:
                dat = get_dat_n()
                index = dat.index(selected_item[0])
                dat[index] = new_value
                put_dat(dat)
                dat = get_dat_n()
                window['listbox'].update(dat)
                window['input_data'].update([])
        case "CLOSE":
            break

window.close()
