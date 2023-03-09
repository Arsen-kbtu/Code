with open("root7.txt") as input, open('dest7.txt', "a") as output:
    for x in input:
        output.write(x)