def find_element_in_tuple(element,tuples):
    new_tuples = ()
    try:
        if isinstance(tuples, tuple):
            for item in tuples:
                if element in item:
                    new_tuples += (item,)

            return new_tuples
        else:
            raise TypeError('L\'element doit etre un tuple')

    except TypeError:
        print('L\'element doit être un tuple')

tuples=\
    (
        (4, 5, 10),
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (10, 11, 12),
        (4, 14, 15),
    )

print(f"Voici ce qu'on a: \n{find_element_in_tuple(4,tuples)}")
