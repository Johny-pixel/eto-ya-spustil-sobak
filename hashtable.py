import os


class Hashtable:
    id_row_dict = {}
    id_year_dict = {}
    ends_of_files = []
    id_deleted_dict = {}

    def __init__(self):
        # os.chdir(r'C:\Users\anton\PycharmProjects\PySimpleGUI-CSV-Tutorial-main')

        os.chdir(r'C:\Users\Euphoria\eto-ya-spustil-sobak')

        with open('contacts.csv', 'r') as file:
            for index, line in enumerate(file):
                if index == 0 or line == '\n':
                    continue
                else:
                    row = line.split(',')
                    self.id_row_dict[int(index)] = int(row[0])
                    self.id_year_dict[int(row[0])] = int(row[4])
                    self.id_deleted_dict[int(row[0])] = False

        self.ends_of_files = fill_ends_of_lines_array()
        print(self.id_row_dict, self.id_year_dict)

    def get_row_by_id(self, id: int) -> int:
        return self.id_row_dict.get(id)

    def get_entry_keys(self):
        return list(self.id_row_dict.keys())

    def get_ids_by_year(self, year: int) -> int:
        ids = []
        for id, year_h in self.id_year_dict.items():
            if year == year_h:
                ids.append(id)
        return ids

    def get_line(self, index):
        with open('contacts.csv', 'r') as file:
            indices = self.ends_of_files
            if index + 1 >= indices.__len__():
                return ''
            else:
                file.seek(indices[index])
                result_line = file.readline()
        return result_line

    def delete_by_id(self, id):
        self.id_deleted_dict[id] = True

    def get_id_deleted(self):
        return self.id_deleted_dict


def fill_ends_of_lines_array():
    new_line_indices = [0]
    with open('contacts.csv', 'r') as file:
        for i, line in enumerate(file):
            last_index = new_line_indices[i]
            if '\n' in line:
                _index = len(line) + 1
                new_line_indices.append(_index + last_index)

    return new_line_indices
