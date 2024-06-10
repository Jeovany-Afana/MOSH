#Ecire une fonction qui prend deux paramètres et qui fait la divisiond es deux nombres, on vérifiera avec des exceptions si b est différent de 0

def division(a,b):
    try:
        if isinstance(a,int) and isinstance(b,int):
            return a/b

        else:
            raise TypeError("Les paramètres doivent être des entiers")
    except TypeError:
        print("Les paramètres doivent être des entiers")
    except ZeroDivisionError:
        print("Division par zéro impossible")
    except NameError:
        print("La variable n'existe pas")
    except SyntaxError:
        print("Erreur de syntaxe")

print(f"La division donne: {division(4,4)}")