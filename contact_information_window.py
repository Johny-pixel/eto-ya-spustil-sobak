import csv
import os

import PySimpleGUI as sg
import pandas as pd

import database_interface


database_interface = database_interface.database_interface()

os.chdir(r'/home/euphoria/eto-ya-spustil-sobak/')


def find_all():
    contact_records = database_interface.find_all()
    return contact_records


def find_by_id(id):
    return database_interface.findById(id)


def find_by_year(year):
    return database_interface.findByYearOfBirth(year)


def delete_by_id(id):
    database_interface.delete(id)


def delete_by_year(year):
    database_interface.deleteByYearOfBirth(year)


def insert(id, name, address, phone_number, year_of_birth, wage, marital_status):
    database_interface.insert(id, name, address, phone_number, year_of_birth, wage, marital_status)


def update(id, name, address, phone_number, year_of_birth, wage, marital_status):
    database_interface.update(id, name, address, phone_number, year_of_birth, wage, marital_status)


def create(type=None, parameter=0):
    if type == 'find all':
        contact_records_array = find_all()
    elif type == 'find by id':
        # ебаш окно на выбор Id -> id
        contact_records_array = find_by_id(parameter)
        print(contact_records_array)
    elif type == 'find by year':
        contact_records_array = find_by_year(parameter)
        print(contact_records_array)

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


def delete():
    id_deleted_dict = database_interface.get_id_deleted_dict()

    print(id_deleted_dict)
    with open('contacts.csv', 'r') as inp, open('first_edit.csv', 'w', newline='') as out:
        writer = csv.writer(out)
        writer.writerow(['Id', 'Name', 'Address', 'Phone Number', 'Year of Birth', 'Wage', 'Engaged'])

        for row in csv.reader(inp):
            if row[0] != 'Id':
                if id_deleted_dict.get(int(row[0])) == False:
                    # if not id_deleted_dict.get(row[0]):
                    writer.writerow(row)


def export_to_xlsx():
    file = pd.read_csv('contacts.csv')
    file.to_excel('export.xlsx')


def set_file(name):
    file = pd.read_csv(name)
    file.to_csv('contacts.csv')
