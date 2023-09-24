# The Perfect Guess 
'''A program that generates a random number and asks the user to guess
it. If the player guesses a higher number, then the program displays
"lower number please". 
Similarly,  if the user guesses a lower number, then the program
displays "higher number please".
When the user guesses the correct number, the program displays the
number of guesses the user took to arrive at the number.'''

# import random 
# # comp = random.randint(1, 10)

# # user = None
# # comp = None

# guesses = 1
# def guessGame(comp, user):
#     while user != comp:
#         if user == comp:
#             print(f"Congratulations!\nYou have guessed the right number! It took you {guesses} guesses")

#         elif user>comp:
#             user = int(input("Incorrect guess. Try a lower number:\n"))
#             guesses += 1
#             return guessGame(comp, user)

#         elif user<comp:
#             user = int(input("Incorrect guess. Try a higher number:\n"))
#             guesses += 1
#             return guessGame(comp, user)

# userInput = int(input("Comp has picked a number! Take a guess:\n"))
# compInput = random.randint(1, 10)
# guessGame(compInput, userInput)

        

        # if user<comp:
        #     user = int(input("Incorrect guess. Try a higher number:\n"))
        #     guess += 1
            # return guessGame(comp, user, guess)



import random 
comp = random.randint(1, 10) 
# print(comp)
print("Comp has picked a number!")

# user = int(input("Comp has picked a number! Take a guess:\n"))


user = None 
guesses = 1
while user != comp: # Initially, user will never be == to comp as user is set
#to 'None' while comp is 1-10 so the while loop will always proceed/run
    user = int(input("Take a guess:\n"))

    if user == comp:
        print(f"You have guessed the right number!")

    else:
        if user>comp:
            print("Incorrect guess. Try a lower number.\n", end ="")
            guesses += 1

        elif user<comp:
            print("Incorrect guess. Try a higher number.\n", end="")
            guesses += 1

print(f"Congratulations! It took you {guesses} guesse(s)")


with open("highscore.txt", 'r') as f:
    highscore = int(f.read())

if guesses<highscore:
    with open("highscore.txt", 'w') as f:
        f.write(str(guesses))
