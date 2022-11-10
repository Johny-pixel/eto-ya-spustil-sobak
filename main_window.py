import PySimpleGUI as sg

import contact_information_window
import database_interface
import generate_csv
import validation
import pandas as pd
import numpy as np
from hashtable import Hashtable


sg.theme('Default')
sg.set_options(font=('Courier 14'))

layout = [[sg.Text("Enter ID:"), sg.Input(key='-ID-', do_not_clear=True, size=(150, 1))],
          [sg.Text("Enter full name:"), sg.Input(key='-NAME-', do_not_clear=True, size=(150, 1))],
          [sg.Text("Enter address:"), sg.Input(key='-ADDRESS-', do_not_clear=True, size=(150, 1))],
          [sg.Text("Enter phone number:"), sg.Input(key='-PHONE_NUMBER-', do_not_clear=True, size=(150, 1))],
          [sg.Text("Enter the year of birth:"), sg.Input(key='-YEAR-OF-BIRTH-', do_not_clear=True, size=(150, 1))],
          [sg.Text("Enter wage:"), sg.Input(key='-WAGE-', do_not_clear=True, size=(150, 1))],
          [sg.Text("Enter marital status:"), sg.Input(key='-MARITAL_STATUS-', do_not_clear=True, size=(150, 1))],
          [sg.Button('Submit Contact Information', expand_x=True), sg.Button('Show Table', expand_x=True),
           sg.Button('Generate CSV', expand_x=True), sg.Button('Update', expand_x=True), sg.Exit()],
          [sg.Text('Finding by ID')], [sg.Input()], [sg.OK('Find by ID')],
          [sg.Text('Finding by the Year of Birth')], [sg.Input()], [sg.OK('Find by the Year of Birth')],
          [sg.Text('Deleting by ID')], [sg.Input()], [sg.OK('Delete by ID')],
          [sg.Text('Deleting By the Year Of Birth')], [sg.Input()], [sg.OK('Delete by the Year of Birth')]
          ]

window = sg.Window("Submit Contact Information", layout).Finalize()
window.Maximize()

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Submit Contact Information':
        validation_result = validation.validate(values)
        if validation_result["is_valid"]:
            database_interface.insert(values['-ID-'], values['-NAME-'], values['-ADDRESS-'], values['-PHONE_NUMBER-'],
                                      values['-YEAR_OF_BIRTH-'], values['-WAGE-'], values['-MARITAL_STATUS-'],
                                      values['-YEAR_OF_BIRTH-'])
            sg.popup("Contact Information submitted!")
        else:
            error_message = validation.generate_error_message(validation_result["values_invalid"])
            sg.popup(error_message)
    elif event == 'Show Table':
        contact_information_window.create('find all')
    elif event == 'Generate CSV':
        generate_csv.create()
    elif event == 'Find by ID':
        print('You chose', values[0])
        contact_information_window.create('find by id', int(values[0]))

    elif event == 'Find by the Year of Birth':
        print('You chose', values[1])



