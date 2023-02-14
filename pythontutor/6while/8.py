n=int(input())
max=n
i=0
y=0
while n!=0:
    if max<n:
        max=n
        y=i
    n=int(input())
    i+=1
print(y)