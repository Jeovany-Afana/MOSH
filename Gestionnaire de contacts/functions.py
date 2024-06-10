import gestion


def add_contact():
    contactname = input('Enter a contact name \n> ')
    contactphone = input('Enter a contact phone \n> ')
    contactemail = input('Enter a contact email \n> ')

    gestion.list_of_contacts = dict([('Name', contactname), ('Contact', contactphone), ('Email', contactemail)])
    gestion.users_list.append(gestion.list_of_contacts)


def show_contact():
    for row in gestion.users_list:
        for k,v in row.items():
            print(f'{k}: {v}')

