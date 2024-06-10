#Créer une fonction qui prend en paramètre un dictionnaire qui contient des noms et des ages et qui retourne le nom de la
#personne la plus agée

def older(dictionnary):
    try:
        if isinstance(dictionnary, dict):

            return dictionnary[max(dictionnary.keys())]
        else:
            raise TypeError('Please the parameter must be a dictionary')
    except TypeError:
        print('Veuillez donner un dictionnaire s\'il vous plait')


dictionary = dict([(29, 'AFANA'), (30, 'ATANGANA'), (31, 'Dylan'), (10, 'Daniele'), (20, 'Kevin')])
print(f'Le plus agé c\'est: {older(dictionary)}')
