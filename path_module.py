from pathlib import Path as File

path = File()  #On crée une instance de la classe Path qui prend en paramètre le répertoire / Fichier que nous voulons utiliseer
#Si on ne passe rien en paramètre, alors la variable path représente notre répertoire actuel
for file in path.glob('*.py'):  #Permet d'afficher tous les fichiers qui ont l'extension .PY
    print(file)
