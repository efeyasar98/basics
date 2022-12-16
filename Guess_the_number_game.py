import random
import time

print("""*******************

Number Guessing Game

Guess The Number From 1 to 40

""")

random_number = random.randint(1,40)
guessing_chance = 7
while True:

    guess_ = int(input("Your guess:"))

    if (guess_ < random_number):
        print("We are checking your guess")
        time.sleep(1)
        print(" Guess a higher number ")
        guessing_chance -= 1

    elif  (guess_ > random_number):
        print("We are checking your guess")
        time.sleep(1)
        print(" Guess a lower number ")
        guessing_chance -= 1
    else:
        print("We are checking your guess")
        time.sleep(1)
        print("Congratulations..!! Our number",random_number)
        break
    if (guessing_chance == 0 ):
        print("Your guess chance is over :) ")
        print(" Our number is:",random_number)
        break