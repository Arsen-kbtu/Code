def tup(tuple):
    for x in tuple:
        if x==False:
            return False
    return True
tuple=("fnjsfkn", 1, True)
print(tup(tuple))