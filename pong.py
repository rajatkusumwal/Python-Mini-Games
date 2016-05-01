# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[0,0]
score1=0
score2=0
paddle1_pos=[0,0]
paddle1_pos=[0,0]
paddle1_vel=[0,0]
paddle2_vel=[0,0]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos,ball_vel# these are vectors stored as listsrandom.randrange(60, 180)
    xv=random.randrange(120, 240)
    yv=random.randrange(60, 180)
    ball_pos=[ WIDTH/2, HEIGHT/2]
    if(direction=="LEFT"):
        ball_vel=[-xv/60,-yv/60]
    elif(direction=="RIGHT"):
        ball_vel=[xv/60,-yv/60]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos=[[0,(HEIGHT/2)-HALF_PAD_HEIGHT],[0,(HEIGHT/2)+HALF_PAD_HEIGHT],[HALF_PAD_WIDTH,(HEIGHT/2)-HALF_PAD_HEIGHT],[HALF_PAD_WIDTH,(HEIGHT/2)+HALF_PAD_HEIGHT]]
    paddle2_pos=[[WIDTH,(HEIGHT/2)-HALF_PAD_HEIGHT],[WIDTH,(HEIGHT/2)+HALF_PAD_HEIGHT],[WIDTH-HALF_PAD_WIDTH,(HEIGHT/2)-HALF_PAD_HEIGHT],[WIDTH-HALF_PAD_WIDTH,(HEIGHT/2)+HALF_PAD_HEIGHT]]	
    spawn_ball("RIGHT")
    score1=score2=0
        
        
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    #colision and reflection
    if(ball_pos[1]<=BALL_RADIUS):
        ball_vel[1]=- ball_vel[1]
    if(ball_pos[1]>=(HEIGHT-BALL_RADIUS)):
        ball_vel[1]=- ball_vel[1]
    if(ball_pos[0]+BALL_RADIUS>=paddle2_pos[2][0] and ball_pos[1]>=paddle2_pos[0][1] and ball_pos[1]<=paddle2_pos[1][1]):
        ball_vel[0]=- ball_vel[0]
        ball_vel[0]+=ball_vel[0]*.1
        ball_vel[1]+=ball_vel[1]*.1
    if(ball_pos[0]-BALL_RADIUS<=paddle1_pos[2][0] and ball_pos[1]>=paddle1_pos[0][1] and ball_pos[1]<=paddle1_pos[1][1]):
        ball_vel[0]=- ball_vel[0]
        ball_vel[0]+=ball_vel[0]*.1
        ball_vel[1]+=ball_vel[1]*.1
    if(ball_pos[0]<=BALL_RADIUS):
        spawn_ball("RIGHT")
        score2+=1
    if(ball_pos[0]>=(WIDTH-BALL_RADIUS)):
        spawn_ball("LEFT")
        score1+=1    
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,2,'White','White')
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[0][1]+=paddle1_vel[1]
    paddle1_pos[1][1]+=paddle1_vel[1]
    paddle1_pos[2][1]+=paddle1_vel[1]
    paddle1_pos[3][1]+=paddle1_vel[1]
    paddle2_pos[0][1]+=paddle2_vel[1]
    paddle2_pos[1][1]+=paddle2_vel[1]
    paddle2_pos[2][1]+=paddle2_vel[1]
    paddle2_pos[3][1]+=paddle2_vel[1]
    
    
        
    # draw paddles
    canvas.draw_polygon(paddle1_pos, 12, 'White', 'Black')
    canvas.draw_polygon(paddle2_pos, 12, 'White', 'Black')
    
    # determine whether paddle and ball collide    
    if(paddle2_pos[0][1]<=0):
        paddle2_pos[0][1]-=paddle2_vel[1]
        paddle2_pos[1][1]-=paddle2_vel[1]
        paddle2_pos[2][1]-=paddle2_vel[1]
        paddle2_pos[3][1]-=paddle2_vel[1]
    elif(paddle2_pos[3][1]>=400):
        paddle2_pos[0][1]-=paddle2_vel[1]
        paddle2_pos[1][1]-=paddle2_vel[1]
        paddle2_pos[2][1]-=paddle2_vel[1]
        paddle2_pos[3][1]-=paddle2_vel[1]
    if(paddle1_pos[0][1]<=0):
        paddle1_pos[0][1]-=paddle1_vel[1]
        paddle1_pos[1][1]-=paddle1_vel[1]
        paddle1_pos[2][1]-=paddle1_vel[1]
        paddle1_pos[3][1]-=paddle1_vel[1]
    elif(paddle1_pos[3][1]>=400):
        paddle1_pos[0][1]-=paddle1_vel[1]
        paddle1_pos[1][1]-=paddle1_vel[1]
        paddle1_pos[2][1]-=paddle1_vel[1]
        paddle1_pos[3][1]-=paddle1_vel[1]
        
    # draw scores
    canvas.draw_text("Player1:"+str(score1), (20, 20), 20, 'White') 
    canvas.draw_text("Player2:"+str(score2), (500, 20), 20, 'White')     
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc=3
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1]-=acc
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1]+=acc
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1]-=acc
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1]+=acc
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    acc=3
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1]+=acc
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1]-=acc
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1]+=acc
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1]-=acc
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
button2 = frame.add_button('Restart Game', new_game, 100)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
