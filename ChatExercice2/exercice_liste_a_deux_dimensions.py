
#Ecrire une fonction qui permet de faire la somme des éléments d'une liste à deux dimansions
def sum_of_matrix(list):
    sum=0
    for row in list:
        for item in row:
            sum += item
    print(f'La somme des elements de la liste à deux dimensions est: {sum}')

liste=\
    [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15]
    ]

sum_of_matrix(liste)
