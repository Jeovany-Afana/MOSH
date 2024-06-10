#Créer une fonction qui prend en paramètre un liste et qui afficher les trois derniers éléments de la liste

def print_last_three_elements(liste):
    try:
        if isinstance(liste,list):
            print(liste[-3:])
        else:
            raise TypeError('Veuillez donner une liste s\'il vous plait')

    except TypeError:
        print('Veuillez donner une liste s\'il vous plait')

liste=[4,7,8,10,34,8,-5]
number=9
name='AFANA'
print_last_three_elements(name)