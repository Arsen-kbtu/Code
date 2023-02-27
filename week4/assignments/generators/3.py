class MyNumbers:
  def __init__(self, n):
    self.n=n
  def __iter__(self):
    self.a = 3
    return self
  def __next__(self):
    if self.a <= self.n:
      x = self.a
      self.a += 1
      if x%3==0 or x%4==0:
       return x
        
    else:
      raise StopIteration
n=int(input())
obj=MyNumbers(n)
var=iter(obj)
for x in var:
    if x!=None:  
     print(x, sep="", end=", ")