a=int(input())
b=int(input())
if a<b:
    for x in range(a, b+1, 2):
        print(x, sep=' ', end=' ')
else:
    for x in range(a, b-1, -2):
        print(x, sep=' ', end=' ')
