import random

MAX_NUM = 100

def main():
    guesses = 0
    rand = random.randint(1, MAX_NUM + 1)
    num = -1
    while num != rand:
        guesses += 1
        num = int(input("guess a number between 1 and " + str(MAX_NUM) + " "))
        if num > rand:
            print("lower")
        elif num < rand:
            print("higher")    
    print("congrats, you got it right in " + str(guesses) + " guesses")
main()
    
    