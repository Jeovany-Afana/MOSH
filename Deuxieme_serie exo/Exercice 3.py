#Créer une fonction qui prend en paramètre une liste de nombres et qui renvoie la somme des éléments pairs de la liste
def sum_of_even_numbers(liste):
   try:
       if isinstance(liste,list):
           sum=0
           for item in liste:
               try:
                   if isinstance(item,int):
                       if item %2 == 0:
                        sum += item
                   else:
                        raise TypeError(f'L\'élément {item} n\'est pas un entier ')
               except TypeError:
                   print('L\'élément {item} n\'est pas un entier')
           return sum
       else:
            raise TypeError('L\'element passé en paramètre doit être une liste')
   except TypeError:
    print('L\'element passé en paramètre doit être une liste')


liste = [3, 8, 'AFANA']
print(f'La somme des elements donne: {sum_of_even_numbers(liste)}')



