#Créer une fonction qui prend une liste de mots en paramètre et qui retourne un dictionnaire dans lequel les mots
#sont les clés et les valeurs sont le nombre d'occurence de chaque mot dans la liste

def list_to_dictionary(liste):
    try:
        if isinstance(liste, list):

            dictionnary = {}

            for element in liste:
              count = liste.count(element)
              dictionnary[element] = count
            return dictionnary
        else:
            raise TypeError('List must be a list')
    except TypeError:
        print('List must be a list')


liste = ['AFANA', 'John', 'AFANA', 'John', 'Damso', 'AFANA', 'John', 'Wilfred']

print(list_to_dictionary(liste))


