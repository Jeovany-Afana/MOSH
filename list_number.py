numbers=[3,0,7,3,-2,9,18,4,8,7,2,4,5,5,6]
#Remove the duplicates in the list
uniques =[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(numbers)
print(uniques)