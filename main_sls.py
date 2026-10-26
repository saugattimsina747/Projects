#number guesser
import random
print("="*40)
print("welcome to the number guessing game ")
print("="*40)
try:
    user_input = int(input("Enter the number you think the computer has guessed between 1-256 : \n"))
#takes the number from the user and saves it in the user_input variable
except(ValueError,NameError):
    print("please enter a valid whole number! \ntry again!")
#this prints the print statement if it finds any of those two errors and exits out of the program entirely
    exit()
print("-"*40)
computer_guess = int(random.randint(1,10))
#this saves a random integer between 1-10 as computers guess
if (user_input == computer_guess):
    print(f"You have guessed the correct answer i.e. {computer_guess}")
elif (user_input != computer_guess):
    print(f"Your guess is incorrect\nThe correct guess is {computer_guess}.\nThank you ")
#prints appropriate message based on guess
print("-"*40)