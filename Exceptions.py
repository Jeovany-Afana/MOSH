import math
try:
    age=int(input("Please enter your age \n"))
    number=200
    division=number/age
    print(f'The age: {round(division,2)}')
except ZeroDivisionError:
    print('You can\'t divide by zero. Please enter your age')
except ValueError:
    print('Invalid age')

