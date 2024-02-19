# Python code for ROCK PAPER SCISSOR game

import random
user=0
comp=0

while True:
    print(" \n>>>>> THE ROCK PAPER & SCISSORS GAME  <<<<< \n")
    print(" -- R for rock , P for paper , S for scissor , Q to quit --   ")
    user_input=input(" => Enter your choice here:  ").lower()
    if user_input=="q":
        print("Okay you quit")
        print("Your score >> ",user)
        print("Computer score >> ",comp)
        break
    else:
        list=["rock","paper","scissor"]
        comp_input=random.choice(list)
                
        print(comp_input)

        if comp_input=="rock" and user_input=="p":
            print(" You win !")
            user += 1
        elif comp_input=="paper" and user_input=="s":
            print(" You win !")
            user += 1
        elif comp_input=="scissor" and user_input=="r":
            print(" You win !")
            user += 1
        elif comp_input=="scissor" and user_input=="s":
            print(" Draw ")
        
        elif comp_input=="rock" and user_input=="r":
            print(" Draw ")
        
        elif comp_input=="paper" and user_input=="p":
            print(" Draw ")
        
        else:
            print("Computer wins !")
            comp += 1
