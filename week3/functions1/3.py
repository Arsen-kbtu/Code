def solve(numheads, numlegs):
    # 2*x+4*y=numlegs
    # x+y=numheads
    # 2*y=numlegs-2*numheads
    y=int((numlegs-2*numheads)/2)
    x=int(numheads-y)
    print("We have ", y, " rabbits and ", x, " chickens")
h=int(input())
l=int(input())
solve(h, l)
