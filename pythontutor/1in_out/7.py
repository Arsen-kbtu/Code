n1=int(input())
n2=int(input())
n3=int(input())
c1=n1//2
c2=n2//2
c3=n3//2
if n1%2==1:
    c1=c1+1
if n2%2==1:
    c2=c2+1
if n3%2==1:
    c3=c3+1
c=c1+c2+c3
print(c)