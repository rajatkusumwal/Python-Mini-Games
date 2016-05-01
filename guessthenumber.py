# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# initialize global variables used in your code
ran = 100
turn = 7
sn = 0


# helper function to start and restart the game
def new_game():
    global sn,ran,turn
    print "New game. Range is from 0 to ",ran
    print "Number of remaining guesses is ",turn
    sn=random.randint(0,ran)
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global ran,turn
    ran=100
    turn=7
    new_game()

def range1000():
    global ran,turn
    ran=1000
    turn=10
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global turn,sn
    print "Guess was ",guess
    g = int(guess)
    turn-=1
    print "Number of remaining guesses is ",turn
    if g<sn:
        print "Higher"
    elif g>sn:
        print "Lower"
    else :
        print "Correct"
        range100()
    if turn==0:
        range100()
                     
        
    
# create frame
f=simplegui.create_frame("Guess The Number",200,200)


# register event handlers for control elements
f.add_button("Range 0-100",range100,200)
f.add_button("Range 0-1000",range1000,200)
f.add_input("Enter a guess",input_guess,200)


# call new_game and start frame
new_game()
f.start()


# always remember to check your completed program against the grading rubric
