import os


class Hashtable:
    id_row_dict = {}
    id_year_dict = {}

    def __init__(self):
        os.chdir(r'C:\Users\anton\PycharmProjects\PySimpleGUI-CSV-Tutorial-main')
        with open('contacts.csv', 'r') as file:
            for index, line in enumerate(file):
                if index == 0 or line == '\n':
                    continue
                else:
                    row = line.split(',')
                    self.id_row_dict[int(index)] = int(row[0])
                    self.id_year_dict[int(row[0])] = int(row[4])

        print(self.id_row_dict, self.id_year_dict)

    def get_row_by_id(self, id: int) -> int:
        print('hui')
        return self.id_row_dict.get(id)

    def get_entry_keys(self):
        return list(self.id_row_dict.keys())
