import math
import tuples

choice=int(input('Faites un choix: \n').strip())
number=22
def exercice1():
    print('*' * 10)

def exercice2():
    number =0
    print('La variable a été rénitialisée')


def exercice5():
    number_one = float(input('Please enter your first number').strip())
    number_two = float(input('Please enter your second number').strip())
    print(f'number_one + number_two= {number_one+number_two}')
    print(f'number_one - number_two= {number_one-number_two}')
    print(f'number_one * number_two= {number_one*number_two}')
    print(f'number_one / number_two= {number_one/number_two}')

def exercice7():
    texte="Je m'appelle Afana Jeovany et je suis le plus beau du Sénégal je n'en doute pas"
    words =texte.split()
    if "Jeo" in texte:
     print(texte.upper())
     print(texte.lower())
     print(len(words))


def exercice9():
   #Utilisation de la méthode replace
   text = 'Bonjour à tous Je m\'appelle Joe et je suis le plus beau'
   print(text.replace('Bonjour','Salut'))


def exercice10():
     #Révivion sur les formated strings et sur l'utilisation de certaines méthodes mathématiques
    number=int(input('Please enter a number'))

    print(f'''
           Votre nombre au carré donne: {number ** 2}
           La valeur absolue de votre nombre est: {math.fabs(number)}
           Le factoriel de votre est de : {math.factorial(number)}
           L'arrondi de votre nombre à deux nombres après la virgule: {round(number,2)}
           
           ''')

def exercice13():
    #Révivions sur la méthode range
    for number in range(13):
        print(number)

def exercice14():
    #Gestion des chaines/tableaux de caractères
    list=['Name', 'Joe', 'John', 'Afana']
    char_list='Je suis etudiant'

    for char in char_list:
        print(char)

    for item in list:
            print(item)

def exercice15():
    #Utilisation de la boucle while
    i=0
    while i<10:
        print(i)
        i+=1

def exercice16():
    #Révision sur l'utilisation de la méthode range
    for x in range(3):
        for y in range(3):
            print(f'({x},{y})')

def exercice17():
    #Revisions sur les méthodes des listes
    list =[3,4,8,5,3,10,4,2,4,35,0,48,46,48,3,2,9,0,4,5]
    not_double=[]
    list.remove(0)
    list.append(255)
    list.sort()
    for number in list:
        if number not in not_double:
            not_double.append(number)
    print(list)
    print(not_double)

def exercice18():
 #Tableau à deux dimentsions // EXERCICE 21
  double_list=\
 [
      [3,5,8,10],
      [4,22,8,0],
      [5,17,7,2],
      [1,18,4,8],
      [7,2,4,5],
      [5,5,6,0]
  ]
  for k,v in enumerate(double_list):
      print(k,v)


  for row in double_list:
      for item in row:
          print(item)

      print("\n")

def exercice19():
    #Les tuples
   tuples = ('Afana ','Jeovany',22,'Computer Science',True)

   for item in tuples:
    print(item)

def exercice20():
    #Les dictionnaires
    dictionary =dict([('Name', 'Afana'),('Email', 'wilfrieddylan@gmail.com'),('Prenom', 'Joe'),('Is_married','False'),('School', 'Supdeco')])

    dictionary['Mignon']='Très mignon'
    for k,v in dictionary.items():
          print(f'{k}: {v}')

def exercice21():
#Exercice pour l'apprentissage des dictionnaires
     phone_number=input('Please enter a phone number')
     numbers=\
    {
          '0': 'Zero',
          '1': 'One',
          '2': 'Two',
          '3': 'Three',
          '4': 'Four',
          '5': 'Five',
          '6': 'Six',
          '7': 'Seven',
          '8': 'Eight',
          '9': 'Nine',
     }


     show_letters =' '
     for element in phone_number:
         show_letters+=numbers[element]+' '

     print(show_letters)

def exercice22():
    #Utilisation de la fonction zip pour parcourir deux listes à la fois
    noms=['Afana','Abe','Atangana','Oum Mbock','NTONGA']
    prenom=['Jeovany', 'Dylan', 'Martini', 'Kevin', 'Daniel']

    for k,v in zip(noms,prenom):
        print(f'Tu t\'appelles {k}  {v}\n'.format(k,v))


def exercice23():
 #Apprentissage de la méthode reverse pour afficher une liste dans l'ordre inverse
 noms = ['Afana', 'Abe', 'Atangana', 'Oum Mbock', 'NTONGA']

 for element in sorted(noms):
     print(element)


def exercice24():

    #Utilisation des méthodes sorted et set pour afficher une séquence en éliminant les doublons
    list = [3, 4, 8, 5, 3, 10, 4, 2, 4, 35, 0, 48, 46, 48, 3, 2, 9, 0, 4, 5]

    for element in sorted(set(list)):
        print (element)

def factorial(number):
     if number<=1:
         return 1

     else:
         return number*factorial(number-1)


def exercice26():

   nombre_premier=int(input('Entrez la limite de nombres premiers que vous voulez afficher: \n'))
   count=0
   nombres_premiers=[]
   for i in  range(1,nombre_premier+1):
       count=0
       for j in range(1,i+1):
           if i%j==0:
               count+=1

       if count==2:
           nombres_premiers.append(i)


   print(nombres_premiers)


def exercice28(list):

    somme=0
    for element in list:
        somme+=element

    return somme





exercice =\
    {
      1: exercice1,
      2: exercice2,
     # 3: exercice3,
     # 4: exercice4,
      5: exercice5,
      #6: exercice6,
      7: exercice7,
      # 8: exercice8,
      9: exercice9,
      10: exercice10,
      # 11: exercice11,
      #12: exercice12,
      13: exercice13,
      14: exercice14,
      15: exercice15,
      16: exercice16,
      17: exercice17,
      18: exercice18,
      19: exercice19,
      20: exercice20,
      21: exercice21,
      22: exercice22,
      23: exercice23,
      24: exercice24,
      25: factorial,
      26: exercice26,
      28: exercice28,
}

if choice in exercice:

    if choice==25: #Cas ou c'est l'exercice sur le factoriel qui est choisi
        number_fact=int(input('Please enter a number for the factorial: \n'))
        print(f'Le factoriel de votre nombre est: {exercice[choice](number_fact)}')

    elif choice == 28:
        list = [3, 7, 12, 9, 34, 20]

        print(f'La somme des éléments de votre liste est: {exercice[choice](list)}')

    else:
        exercice[choice]()
else:
    print('Vous n\'avez pas choisi un exercice valide')

