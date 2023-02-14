from itertools import permutations

def permut():
    word = input()
    perm = permutations(word)
    for i in list(perm):
        print(i)

permut()