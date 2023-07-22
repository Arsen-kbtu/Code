def rev():
    string=input()
    lst=string.split()
    lst.reverse()
    for x in lst:
        print(x, sep=' ', end=' ')
rev()