def unique(list):
    uni=[]
    for x in range(0, len(list)):
        if not list[x] in uni:
            uni.append(list[x])
    print(uni)


a=input()
list=a.split()    
unique(list)