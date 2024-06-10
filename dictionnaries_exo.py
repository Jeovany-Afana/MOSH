numbers={
    0: 'zero',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
}

user_phone=input('Please enter your phone number \n')
output=''
for item in user_phone:
   if int(item) in numbers:
        output+=(' '+numbers[int(item)])
output+=' !'
print(output)