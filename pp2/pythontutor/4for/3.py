a=int(input())
b=int(input())
for x in range(a-int(a%2==0), b-1, -2):
    print(x, sep=' ', end=' ')
