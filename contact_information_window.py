import PySimpleGUI as sg

import database_interface


def find_all():
    contact_records = database_interface.find_all()
    return contact_records


def find_by_id(id):
    return database_interface.findById(id)

def create(type=None, parameter = 0):
    if type == 'find all':
        contact_records_array = find_all()
    elif type == 'find by id':
        #ебаш окно на выбор Id -> id
        contact_records_array = find_by_id(parameter)
    else:
        contact_records_array = []
    headings = ['Id', 'Name', 'Address', 'Phone Number', 'Year of Birth', 'Wage', 'Engaged']

    contact_information_window_layout = [
        [sg.Table(values=contact_records_array, headings=headings, max_col_width=35,
                  auto_size_columns=True,
                  justification='right',
                  num_rows=10,
                  key='-TABLE-',
                  row_height=35,
                  tooltip='Reservations Table')]
    ]

    contact_information_window = sg.Window("Contact Information Window", contact_information_window_layout, modal=False)

    while True:
        event, values = contact_information_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    contact_information_window.close()
