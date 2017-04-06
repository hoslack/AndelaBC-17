def find_missing(array1, array2):
    if not isinstance(array1, list) and not isinstance(array2, list):
        raise TypeError
    elif array1 == array2:
        return 0
    elif not array1 or not array2:
        return 0
    else:
        result = set(array1) ^ set(array2)
        return list(result)[0]

