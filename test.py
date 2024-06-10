try:
    div=10
    number=int(input('Please enter a number\n').strip())
    print(f"Le nombre est: {div/number}")

except ZeroDivisionError:
    print('Le nombre ne doit pas être nul')

except ValueError:
    print('Le nombre doit être un entier')