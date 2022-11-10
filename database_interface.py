import os

from hashtable import Hashtable
import pandas as pd

os.chdir(r'C:\Users\anton\PycharmProjects\PySimpleGUI-CSV-Tutorial-main')

hashtable = Hashtable()


def insert():
    pass


def findById(id: int):
    rows = hashtable.get_entry_keys()
    pd.read_csv('contacts.csv',
                skiprows=rows[:hashtable.get_row_by_id(id)-2:] + rows[hashtable.get_row_by_id(id):]).to_csv('result'
                                                                                                              '.csv',
                                                                                                          header=False,
                                                                                                          index=False)

    with open('result.csv', 'r') as file:
        array = []
        for index, line in enumerate(file):
            if index == 0 or line == '\n':
                continue
            else:
                row = line.split(',')
                array.append(row)
    return array


def findByYearOfBirth():
    pass


def find_all():
    with open('contacts.csv', 'r') as file:
        array = []
        for index, line in enumerate(file):
            if index == 0 or line == '\n':
                continue
            else:
                row = line.split(',')
                array.append(row)
    return array


def update():
    pass


def delete():
    pass


def deleteByYearOfBirth():
    pass
