import math
n=int(input())
a=int(input())
p=a*n
tg=math.tan(math.pi/n)
ap=a/(2*tg)
s=int((ap*p)/2)
print(s)
