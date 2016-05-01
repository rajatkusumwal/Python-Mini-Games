# template for "Stopwatch: The Game"
import simplegui


# define global variables
count=0
a="0"
b="0"
c="0"
d="0"
a1=0
b1=0
c1=0
d1=0
x=0
y=0
x1=0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global count,a,b,c,d,a1,b1,c1,d1
    d1=count%10
    c1=(count%100)/10
    b1=(count%1000)/100
    if b1==6:
        a1=a1+1
        count=0
    a=str(a1)
    b=str(b1)
    c=str(c1)
    d=str(d1)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def fstart():
    global x1
    x1=0
    timer.start()
    
def freset():
    global count,a1,x,y
    count=0
    a1=0
    x=0
    y=0

def fstop():
    global b1,x,y,x1
    timer.stop()
    if c1==5 and d1==0 and x1==0:
        x+=1
        y+=1
    elif x1==0:
        y+=1
    x1=1
    
# define event handler for timer with 0.1 sec interval
def time():
    global count
    count=count+1
    format(count)
    
    
# define draw handler
def draw(canvas):
    s=a+':'+b+c+':'+d
    s1="Reflex Game : "+str(x)+"/"+str(y)
    canvas.draw_text(s, [250, 150], 20, 'Blue')
    canvas.draw_text(s1,[50,50],20,'Red')
    
# create frame
frame=simplegui.create_frame("Stopwatch",500,300)

# register event handlers

timer=simplegui.create_timer(100,time)
frame.set_draw_handler(draw)
start = frame.add_button('Start',fstart,50)
reset = frame.add_button('Reset',freset,50)
stop = frame.add_button('Stop',fstop,50)

# start frame
frame.start()


# Please remember to review the grading rubric
