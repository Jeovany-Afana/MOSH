import sys as system
users_list = [
    {
        'Name': 'AFANA',
        'Contact': '774931623',
        'Email': 'wilfrieddylan@gmail.com',
    }]
list_of_contacts = {}
contact_found = False


def add_contact() -> None:
    global users_list
    global list_of_contacts
    contactname = input('Enter a contact name \n> ').strip().upper()
    contactphone = input('Enter a contact phone \n> ').strip()
    contactemail = input('Enter a contact email \n> ').strip()

    list_of_contacts = dict([('Name', contactname), ('Contact', contactphone), ('Email', contactemail)])
    users_list.append(list_of_contacts)
    print('Contact added successfully !')


def show_contact() -> None:
    for row in users_list:
        for k, v in row.items():
            print(f'{k}: {v}')


def search_contact(type_of_search: str, searched_name: str = None, contact_list: list = None) -> dict:
    contacts_informations = ()

    if contact_list is None:
        contact_list = users_list

    if type_of_search.lower() == 'a':
        if searched_name is None:
            searched_name = input('Please enter the name of the contact you want to search: \n').strip().upper()

        for row in contact_list:
            if row['Name'].upper() == searched_name.upper():
                contacts_informations = row

    elif type_of_search.lower() == 'b':
        phone_number = input('Please enter a phone number').strip()
        for row in contact_list:
            if row['Contact'] == phone_number:
                contacts_informations = row

    if contacts_informations is None:
        print('Contact not found')

    return contacts_informations if contacts_informations else None


def update_contact(information_to_update: str, updated_name: str = None, contacts_list: list = None) -> None:
    if contacts_list is None:
        contacts_list = users_list

    if information_to_update == 'a':
        if updated_name is None:
            updated_name = input('Please enter the name of the contact you want to update: \n').strip().upper()

        for row in contacts_list:
            if row['Name'].upper() == updated_name.upper():
                row['Name'] = input('Please enter the new name of the contact: \n').strip().upper()
                print('Contact updated successfully!')

    elif information_to_update == 'b':
         if updated_name is None:
            updated_name = input('Please enter the name of the contact you want to update: \n').strip().upper()

         for row in contacts_list:
            if row['Name'].upper() == updated_name.upper():
                row['Contact'] = input('Please enter the new phone number of the contact: \n').strip()
                print('Contact updated successfully!')

    elif information_to_update == 'c':
      if updated_name is None:
            updated_name = input('Please enter the name of the contact you want to update: \n').strip().upper()

      for row in contacts_list:
             if row['Name'].upper() == updated_name.upper():
                 row['Email'] = input('Please enter the new email of the contact: \n').strip()
                 print('Contact updated successfully!')


def delete_contact(contact_name: str = None, contact_list: list = None) -> None:
    contact_information = {}
    if contact_list is None:
        contact_list = users_list

    if contact_name is None:
        contact_name = input('Please enter a the name of the contact you want to delete\n').strip()
        for row in contact_list:
            if row['Name'].upper() == contact_name.upper():
                contact_information = row
                contact_list.remove(row)
                print(f'''
                         You're going to delete {contact_information['Name']} ({contact_information['Contact']}) mail: {contact_information['Email']}
                      \n''')
                print('Contact deleted successfully!')


def save_contacts() -> None:
    with open('contacts.txt', 'w') as file:
        for row in users_list:
            file.write(f'{row['Name']}  {row["Contact"]}  {row["Email"]}\n')


def load_contacts_from_text_file() -> None:
    with open('contacts.txt', 'r') as file:
        for row in file:
            row = row.strip().split()
            users_list.append(dict([('Name', row[0]), ('Contact', row[1]), ('Email', row[2])]))


def exit_program():
    print('Bye bye 👋')
    system.exit()

def delete_contact_file():
    with open('contacts.txt', 'w') as file:
        file.write('')
operations =\
    {
      1: add_contact,
      2: show_contact,
      3: search_contact,
      4: update_contact,
      5: delete_contact,
      6: save_contacts,
      7: load_contacts_from_text_file,
      8: exit_program,
      9: delete_contact_file,
    }
