import random
import time
def new_game():
        print("Computer's turn...")
        com = random.randint(1,3)
        time.sleep(.5)
        print("Your turn...")
        time.sleep(.5)
        you = input("Please enter 'r' for rock,'p' for paper or 's' for scissors:")
        if(com==1):
                winner('r',you)
        elif(com==2):
                winner('p',you)
        else:
                winner('s',you)

def nextgame():
        s = input("Press 0 for exit and press any other key for other game:")
        if(s=="0"):
                print("Thank you for playing our game.")
        else:
                new_game()
                

def winner(com,you):
        print(f"Computer chose {com} and You chose {you}")
        if(com==you):
                print("It's a draw.")
                nextgame()
        if(com=='r'):
                if(you =='p'):
                        print("Hurray,you won!!!")
                        nextgame()
                else:
                        print("You lose,Better luck next time!!!")
                        nextgame()
        elif(com=='p'):
                if(you =='s'):
                        print("Hurray,you won!!!")
                        nextgame()
                else:
                        print("You lose,Better luck next time!!!")
                        nextgame()
        elif(com=='s'):
                if(you =='r'):
                        print("Hurray,you won!!!")
                        nextgame()
                else:
                        print("You lose,Better luck next time!!!")
                        nextgame()

print("Welcome to the online rock,paper and scissor game....")
time.sleep(.5)
new_game()


