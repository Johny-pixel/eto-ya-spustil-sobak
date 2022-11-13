import os

import hashtable
import pandas as pd

#os.chdir(r'C:\Users\anton\PycharmProjects\PySimpleGUI-CSV-Tutorial-main')

os.chdir(r'C:\Users\Euphoria\eto-ya-spustil-sobak')



class database_interface:

    def __init__(self):
        self.hashtable = hashtable.Hashtable()



    def insert(self):
        pass


    def findById(self, id: int):
        result_array = []
        result_array.append(self.hashtable.get_line(id).split(','))
        return result_array




    def findByYearOfBirth(self, year: int):
        rows_to_read = self.hashtable.get_ids_by_year(year)

        result_array = []
        for row in rows_to_read:
            result_array.append(self.hashtable.get_line(row).split(','))
        return result_array


    def find_all(self):
        with open('contacts.csv', 'r') as file:
            array = []
            for index, line in enumerate(file):
                if index == 0 or line == '\n':
                    continue
                else:
                    row = line.split(',')
                    array.append(row)
        return array


    def update(self):
        pass


    def delete(self, id):
        self.hashtable.delete_by_id(id)


    def get_id_deleted_dict(self) -> dict:

        return self.hashtable.get_id_deleted()

    def deleteByYearOfBirth(self, year):
        print(year)
        ids_to_delete = self.hashtable.get_ids_by_year(year)
        print(ids_to_delete)

        for id in ids_to_delete:
            self.hashtable.delete_by_id(id)

