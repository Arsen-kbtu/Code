class MyClass:
    def __init__(self):
        self.s=""
    def getString(self):
        self.s=input()
    def printString(self):
        print(self.s.upper())
word=MyClass()
word.getString()
word.printString()