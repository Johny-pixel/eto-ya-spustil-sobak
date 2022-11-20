import PySimpleGUI as sg

import contact_information_window
import generate_csv
import validation

sg.theme('Default')
sg.set_options(font='Courier 14')

layout = [[sg.Text("Enter ID:"), sg.Input(key='-ID-', do_not_clear=True, size=(150, 1))],
          [sg.Text("Enter full name:"), sg.Input(key='-NAME-', do_not_clear=True, size=(150, 1))],
          [sg.Text("Enter address:"), sg.Input(key='-ADDRESS-', do_not_clear=True, size=(150, 1))],
          [sg.Text("Enter phone number:"), sg.Input(key='-PHONE_NUMBER-', do_not_clear=True, size=(150, 1))],
          [sg.Text("Enter the year of birth:"), sg.Input(key='-YEAR_OF_BIRTH-', do_not_clear=True, size=(150, 1))],
          [sg.Text("Enter wage:"), sg.Input(key='-WAGE-', do_not_clear=True, size=(150, 1))],
          [sg.Text("Enter marital status:"), sg.Input(key='-MARITAL_STATUS-', do_not_clear=True, size=(150, 1))],
          [sg.Button('Submit Contact Information', expand_x=True), sg.Button('Show Table', expand_x=True),
           sg.Button('Import from CSV', expand_x=True), sg.Button('Update', expand_x=True), sg.Button('Export to XLSX'),
           sg.Exit()],
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
        contact_information_window.delete()
        break
    elif event == 'Submit Contact Information':
        validation_result = validation.validate(values)
        if validation_result["is_valid"]:
            print(values)
            contact_information_window.insert(values['-ID-'], values['-NAME-'], values['-ADDRESS-'],
                                              values['-PHONE_NUMBER-'],
                                              values['-YEAR_OF_BIRTH-'], values['-WAGE-'], values['-MARITAL_STATUS-'])
            print(values)
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
        contact_information_window.create('find by year', int(values[1]))
    elif event == 'Delete by ID':
        contact_information_window.delete_by_id(int(values[2]))
        sg.popup("Deleted!")
    elif event == 'Delete by the Year of Birth':
        contact_information_window.delete_by_year(int(values[3]))
        sg.popup("Deleted!")
    elif event == 'Update':
        contact_information_window.update(values['-ID-'], values['-NAME-'], values['-ADDRESS-'],
                                          values['-PHONE_NUMBER-'],
                                          values['-YEAR_OF_BIRTH-'], values['-WAGE-'], values['-MARITAL_STATUS-'])
        sg.popup('Updated!')
    elif event == 'Export to XLSX':
        contact_information_window.export_to_xlsx()
    elif event == 'Import from CSV':
        name = sg.popup_get_text('Enter file name *.csv')
        contact_information_window.set_file(name)
