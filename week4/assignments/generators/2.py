class MyNumbers:
  def __init__(self, n):
    self.n=n
  def __iter__(self):
    self.a = 0
    return self
  def __next__(self):
    if self.a <= self.n:
      x = self.a
      self.a += 2
      return x
    else:
      raise StopIteration
n=int(input())
obj=MyNumbers(n)
var=iter(obj)
for x in var:
  print(x, sep=", ", end=" ")