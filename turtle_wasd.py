import turtle

turtle.shape('turtle')

def restart():
    turtle.reset()

def move_up():
    global y
    
def move_down():
    global y
     
def move_left():
    global x
     
def move_right():
    global x


turtle.onkey(move_up,'w')
turtle.onkey(move_down,'s')
turtle.onkey(move_left,'a')
turtle.onkey(move_right,'d')
turtle.onkey(restart,'Esc')
turtle.listen()
turtle.mainloop
