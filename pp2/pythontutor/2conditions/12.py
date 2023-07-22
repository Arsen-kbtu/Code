N=int(input())
M=int(input())
x=int(input())
y=int(input())
if x<N-x and x<y:
    print(x)
if x>N-x and x<y:
    print(N-x)
if y>M-y and x>y:
    print(M-y)
if y<M-y and x>y:
    print(y)
