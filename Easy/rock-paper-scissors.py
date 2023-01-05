# A rock-paper-scissors game:
# Write a program that allows the user to play a game of rock-paper-scissors against the computer.
# You can use the random module to generate the computer's move.

import random

# counters
draw = 0
win = 0 
lose = 0

print("------------------------\nRock-Paper-Scissors!")

while(True):
    try:
        print("\n------------------------\nWins:",win,"Lose:",lose,"Draw:",draw,"\n------------------------")
        x = int(input("1. Rock\n2. Paper\n3. Scissors\n4. Exit\nChoose:"))
        

    except ValueError:
        print("\nError: An integer between 1 and 4 should be provided!\n")

    except KeyboardInterrupt:
        print("\nClosing game.\n")
        break

    else:
        # generate random between 0-2
        y = random.randint(0,2)
        
        ### Player chose rock
        # rock x rock
        if(x == 1 and y==0):
            print("Computer chose rock too! A draw!")
            draw+=1

        # rock x paper 
        elif(x==1 and y==1):
            print("Computer chose paper! You lose!")
            lose+=1

        # rock x scissors
        elif(x==1 and y==2):
            print("Computer chose scissors! You win!")
            win+=1    
        
        ### Player chose paper
        # paper x rock
        elif(x == 2 and y==0):
            print("Computer chose rock! You win!")
            win+=1

        # paper x paper 
        elif(x==2 and y==1):
            print("Computer chose paper too! A draw!")
            draw+=1

        # paper x scissors
        elif(x==2 and y==2):
            print("Computer chose scissors! You lose!")
            lose+=1

        ### Player chose scissors
        # scissors x rock
        elif(x == 3 and y==0):
            print("Computer chose rock! You lose!")
            lose+=1

        # scissors x paper 
        elif(x==3 and y==1):
            print("Computer chose paper! You win!")
            win+=1

        # scissors x scissors
        elif(x==3 and y==2):
            print("Computer chose scissors too! A draw!")
            draw+=1

        elif(x==4):
            print("\nClosing game.\n")
            break    

        else:
            print("\nError: An integer between 1 and 4 should be provided!\n")
            #break


