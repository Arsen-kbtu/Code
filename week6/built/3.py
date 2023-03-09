def pal(txt):
    i=0
    j=len(txt)-1
    while(i<=j):
        if txt[i]!=txt[j]:
            print("not")
            return
        i+=1
        j-=1
    print("valid")

txt=input()
x=pal(txt)