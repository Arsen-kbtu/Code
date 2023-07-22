def has_33(list):
    for x in range(0, len(list)-1):
        if list[x]==3 and list[x+1]==3:
            return True
            break
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3]))
