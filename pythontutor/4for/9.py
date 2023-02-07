N=int(input())
lst=[]
for x in range(1, N+1):
    n=int(input())
    lst.append(n)
c=0
for x in lst:
    if x==0:
        c+=1
print(c)

