n=int(input())
i=0
n1=n+1
while n!=0:
    if n>n1:
        i+=1
    n1=n
    n=int(input())
print(i)