# implementation of card game - Memory

import simplegui
import random

card_deck=[0,1,2,3,4,5,6,7]
card_deck2=[0,1,2,3,4,5,6,7]
card_deck.extend(card_deck2)
expose=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
click=[]
turn=0
counter=0

# helper function to initialize globals
def new_game():
    global expose,counter
    expose=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    random.shuffle(card_deck)
    counter=0
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global click,counter
    expose[pos[0]/50]=True
    counter+=1
    check=pos[0]/50 in click
    if(check==False):
        click.append(pos[0]/50)
    if(len(click)>2):
        a1=click.pop(0)
        a2=click.pop(0)
        if(card_deck[a1]!=card_deck[a2]):
            expose[a1]=False
            expose[a2]=False
    label.set_text("Turns = "+str(counter/2))
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    v=0
    p=[[0,0],[50,0],[50,100],[0,100]]
    for value in range(16):
        if(expose[value] == True):
            canvas.draw_text(str(card_deck[value]), (v*50,100), 60, 'White')
        else:
            canvas.draw_polygon(p,1 , 'Black', 'Green')
        for v1 in range(4):
            p[v1][0]+=50
        v+=1
    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric