#Créer une fonction qui prend en paramètre deux listes de même taille et qui retourne un dictionnaire dans lequel est clés
#sont les éléments de la première liste et les valeurs les éléments de la deuxième liste
def exercice24(liste1,liste2):
    try:
        if isinstance(liste1, list) and isinstance(liste2, list) and len(liste1) == len(liste2):
            dictionnaire={}
            for i in range(len(liste1)):
                dictionnaire[liste1[i]]=liste2[i]
            print(dictionnaire)
        else:
            raise TypeError('Les listes doivent être de même taille')
    except TypeError:
        print('Les listes doivent être de même taille')


names = ['AFANA', 'John', 'Martin', 'Kevin']
ages = [22, 24, 25, 40]

exercice24(liste1=names, liste2=ages)
