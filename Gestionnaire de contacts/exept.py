def try_function(element=None, element_type=None) -> bool:
    try:
        if isinstance(element, element_type):
            return True
        else:
            raise TypeError('Type Error please enter a correct element')
    except TypeError:
        return False
