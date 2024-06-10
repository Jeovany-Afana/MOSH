import operations
from exept import try_function


menu =\
 '''
\t\t\t\t\tMAKE A CHOICE
\t1- Add a new contact
\t2- Show all saved contacts
\t3- Search for a contact by name or phone number
\t4- Update information for an existing contact
\t5- Delete a contact
\t6- Save a contact in a text file
\t7- Load the contact list from a text file
\t8- Exit

      Please make a choice
'''

search_options_menu =\
 '''
  \t\t\t\t\tHOW DO YOU WANT TO SEARCH YOUR CONTACT?
  \ta- Search by name
  \tb- Search by phone number
'''

update_options_menu =\
 '''
  \t\t\t\t\tHOW DO YOU WANT TO UPDATE YOUR CONTACT?
  \ta- Update name
  \tb- Update phone number
  \tc- Update email
  '''
while True:
    print(menu)
    choice = int(input('> ').strip())
    if try_function(choice, int): #On vérifie si le type de la fonction correspond au type attendu
        if choice in operations.operations: #On vérifie si la valeur entrée correspond à une des clés du dictionnaire
            if choice == 3:
                print(search_options_menu)
                newChoice = input('> ').strip()
                if newChoice == 'a' or newChoice == 'b':
                    if operations.operations[3](newChoice) is not None:
                        search_results = operations.operations[3](newChoice)
                        print(f'''
                         
                               Here are the informations of your contacts:
                               
                               Name: {search_results['Name']}
                               Phone number: {search_results['Contact']}
                               Email: {search_results['Email']}
                              ''')
                    else:
                        print('No contact found')

                else:
                    print('Please choose between "a" and "b"')
            elif choice == 4:
                print(update_options_menu)
                newChoice = input('> ').strip()
                if newChoice == 'a' or newChoice == 'b' or newChoice == 'c':
                    operations.operations[4](newChoice)

                else:
                    print('Please choose between "a", "b" and "c"')
            else:
                operations.operations[choice]()

        else:
            print('Please choose between "1" and "8"')
    operations.operations[2]()
