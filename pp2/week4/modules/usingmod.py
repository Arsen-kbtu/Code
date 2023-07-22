import mymodule as mx
import platform
mx.greeting("Jonathan")

a = mx.person1["age"]
print(a)

x = platform.system()
print(x)

x = dir(platform)
print(x)

#from mymodule import person1
#print (person1["age"])