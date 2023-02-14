import random
def game():
    x=random.randint(1, 20)
    print("Hello! What is your name?")
    name=input()
    print(("Well, {}, I am thinking of a number between 1 and 20.\nTake a guess.").format(name))
    n=int(input())
    i=1
    while n!=x:
        if n>x:
            print("Your guess is too great.\nTake a guess.")
        else:
            print("Your guess is too low.\nTake a guess.")
        n=int(input())
        i+=1
    print(("Good job, {}! You guessed my number in {} guesses!").format(name, i))
game()