import random

# A guessing game: 
# Write a program that generates a random number and then prompts the user to guess the number. 
# The program should tell the user whether their guess is too high, too low, or correct.

print("\nGuess the number between 0-100.\n")

rand = random.randint(0,100)
#print("Random number: ", rand)

x=-1

while(x!=rand):
    x = int(input("Give number: "))
    if(x<rand):
        print("It's bigger.")
    else:
        print("It's smaller.")

print(x, "- Congrats, you guessed it!")