class Parent1:
    word1=""
    def __init__(self, color1, number1):
        self.color1=color1
        self.number1=number1
    def printInfo1(self):
        print(self.color1, " ", self.number1)
    def setWord1(self):
        self.word1=input()
    def getWord1(self):
        print(self.word1)
class Parent2:
    word2=""
    def __init__(self, color2, number2):
        self.color2=color2
        self.number2=number2
    def printInfo2(self):
        print(self.color2, " ", self.number2)
    def setWord2(self):
        self.word2=input()
    def getWord2(self):
        print(self.word2)
class BabyBoy(Parent1, Parent2):
    word3=""
    # def __init__(self, color1, number1, color2, number2, word1, word2):
    def __init__(self, color1, number1, color2, number2):
        Parent1.__init__(self, color1, number1)
        Parent2.__init__(self, color2, number2)
        
        self.color3=color1+color2
        self.number3=number1+number2
        
    def printInfo3(self):
        print(self.color3, " ", self.number3)
    def getWord3(self, word1, word2):
        print(word1+word2)
# p1=Parent1("Red", 21)
# #p1.printInfo1()
# p1.setWord1()
# p2=Parent2("Blue", 25)
# #p2.printInfo2()
# p2.setWord2()          
# b=BabyBoy(p1.color1, p1.number1, p2.color2, p2.number2, p1.word1, p2.word2)
b=BabyBoy("color1", 1, "color2", 2)
b.printInfo3()
b.getWord3("word1", "word2")
   