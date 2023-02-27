class squares:
  def __init__(self, a, b):
    self.a=a
    self.b=b
  def __iter__(self):
    self.i = 3
    return self
  def __next__(self):
    if self.a <= self.b:
      x = self.a
      self.a += 1
      return x**2
        
    else:
      raise StopIteration
a=int(input())
b=int(input())
obj=squares(a,b)
var=iter(obj)
for x in var:      
  print(x, sep="", end=", ")