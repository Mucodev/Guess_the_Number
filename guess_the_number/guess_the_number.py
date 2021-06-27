import random   
import os

def start():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    a = random.choice(numbers)

    guess = a

    def again():
        print("Do You Want to Try Again? (y/n)")

        b = input(">")

        if b == "y":
            return start()
        elif b == "n":
            quit()
        else:
            print("Y or N")
            return again()

    def game():
        
        limit = 0

        while True:


            user_guess = input("Enter Your Guess ")


            if int(guess) == int(user_guess):
                print("You Won!")              
                again()

            elif user_guess != guess:
                print("Your Guess is Wrong, Please Try Again")
                limit += 1

                print(f"You Have {3 - int(limit)} left")

            if int(limit) > 3:
                print("Game Over :(")
                
                again()
    
    game()

start()