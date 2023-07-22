def isPrime(ls):
    return list(filter(lambda x: all(x%i != 0 for i in range(2, x)) and x>= 2, ls))
list=[]
print(isPrime(list))