import FreeSimpleGUI as sg
from PROJECTS.Impruve_First_project.With_Interface.Functions import get_dat_n, put_dat
import os

file_path = 'D:\\My_DOC\\data_text\\list_info.txt'

# Define the layout of the window
layout = [
    [sg.Text("Input data")],
    [sg.InputText(key='input_data'),
     sg.Button("ADD")],
    [sg.Listbox(values=[], size=(50, 10), key='listbox')],
     [sg.Button("EDIT"),
     sg.Button("SHOW"),
     sg.Button("DELETE")]
]

# Create the window
window = sg.Window('CRUD Projects', layout, font=('Helvetica', 12))

while True:
    event, values = window.read()
    match event:
        case "ADD":  # INSERT OPERATION
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

        case "SHOW":  # INSERT OPERATION
            if os.path.exists(file_path):
                dat = get_dat_n()
                window['listbox'].update(dat)
            else:
                window['listbox'].update([])

        case "DELETE":  # DELETE DATA FROM LIST
            selected_item = values['listbox']
            if selected_item:
                dat = get_dat_n()
                dat.remove(selected_item[0])
                put_dat(dat)
                window['listbox'].update([])
                dat = get_dat_n()
                window['listbox'].update(dat)

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


window.close()
