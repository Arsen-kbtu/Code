def spy_game(list):
    for x in range(0, len(list)-1):
        if list[x]==0:
            for i in range(x+1, len(list)-1):
                if list[i]==0:
                    for j in range(i+1, len(list)):
                        if list[j]==7:
                            return True
                            break  
    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))