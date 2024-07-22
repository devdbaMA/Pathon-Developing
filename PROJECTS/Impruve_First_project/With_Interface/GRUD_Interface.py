from PROJECTS.Impruve_First_project.With_Interface.Functions import get_dat, get_dat_n, put_dat
import time
import os

import FreeSimpleGUI as sg

lable = sg.Text("Input data")
input_box = sg.InputText("")
add_btn = sg.Button("ADD")

windows = sg.Window('CRUD Projects', [[lable], [input_box, add_btn]])
windows.read()
windows.close()