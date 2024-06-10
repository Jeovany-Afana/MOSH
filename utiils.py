def find_max(list):
    max=list[0]

    for item in list[1:]:
        if item >max:
            max=item
    print(f'The most big element of the list is {max}')