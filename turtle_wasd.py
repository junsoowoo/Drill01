import turtle

turtle.shape('turtle')
speed=50
x,y=0,0
def restart():
    turtle.reset()

def move_up():
    global y
    y += speed
def move_down():
    global y
    y -= speed
def move_left():
    global x
    x -= speed
def move_right():
    global x
    x += speed

turtle.onkey(move_up,'w')
turtle.onkey(move_down,'s')
turtle.onkey(move_left,'a')
turtle.onkey(move_right,'d')
turtle.onkey(restart,'Esc')
turtle.listen()
turtle.mainloop
