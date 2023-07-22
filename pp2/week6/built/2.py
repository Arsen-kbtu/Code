txt="BnnjfehbfjbJVBDNknknkjnf"
u=0
l=0
for x in txt:
    if x.isupper():
        u+=1
    else:
        l+=1
print(u, " ", l)