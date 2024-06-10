names= ['Joe', 'John', 'Afana', 'Wilfred', 'Abanda', 'Junior']
#Find the largest element in the list

elemnt_size=len(names[0])
element_value=names[0]

for item in names[1:]:
       if elemnt_size < len(item):
           elemnt_size=len(item)
           element_value=item
print(f'The largest element in the list is {element_value.upper()}')