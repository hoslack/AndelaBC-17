def find_max_min(n):
    mylist = []
    if not isinstance(n, list):
        raise TypeError
    elif max(n) == min(n):
        mylist.append(len(n))
        return mylist
    else:
        mylist.append(min(n))
        mylist.append(max(n))
    return mylist

