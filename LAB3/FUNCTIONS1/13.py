import random

def Guess_the_number():
    n = random.randrange(1, 20)
    s = input("Hello! What is your name?\n")
    print()
    print(f'Well, {s}, I am thinking of a number between 1 and 20.')
    cnt =1
    while 1 :
        x = input("Take a guess.\n")
        print()
        if (int(x) == n):
            print(f'Good job, {s}! You guessed my number in {cnt} guesses!')
            return 
        elif int(x) < n:
            print("Your guess is too low.")
            cnt += 1
        else:
            print("Your guess is too high.")
            cnt += 1
    
Guess_the_number()
