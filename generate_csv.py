import csv

import database_interface


def get_contact_records():
    contact_records = database_interface.find_all()
    return contact_records


def create():
    contact_records_array = get_contact_records()
    headings = ['Name', 'Address', 'Phone Number', 'Year of Birth']

    file = open('contacts.csv', 'w', encoding='UTF8', newline='')
    writer = csv.writer(file)

    # write the header
    writer.writerow(headings)

    # write multiple rows
    writer.writerows(contact_records_array)
    file.close()
