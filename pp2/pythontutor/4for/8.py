sum=0
fac=1
N=int(input())
for x in range(1, N+1):
    fac*=x
    sum+=fac
print(sum)
