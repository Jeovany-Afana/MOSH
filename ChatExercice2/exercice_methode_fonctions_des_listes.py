#Ecrire une fonction qui prend en paramètre deux listes et qui les fusionne, élimine les doublons, les tries par ordre croissant et renvoie la nouvelle liste fusionnée

def merge_list(liste1,liste2):

    try:
        if isinstance(liste1,list) and isinstance(liste2,list):
            liste3=[]
            liste3=sorted(set(liste1))+sorted(set(liste2))


            print(f'Voici votre liste finale: {sorted(set(liste3))}')


        else:
            raise TypeError('Les deux paramètres doivent être des listes')

    except TypeError:
         print('Les deux paramètres doivent être des listes')

liste1=[2,5,5,8,9,10,25,2]
liste2=[2,34,8,45,10,4,11]

merge_list(liste1,liste2)