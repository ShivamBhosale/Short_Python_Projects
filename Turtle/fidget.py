from turtle import *
state ={'turn':0}

def spinner():
    clear()
    angle= state['turn']/10
    right(angle)
    forward(100)
    dot(120,'Orange')
    back(100)
    right(120)
    forward(100)
    dot(120,'White')
    back(100)
    right(120)
    forward(100)
    dot(120,'Green')
    back(100)
    right(120)
    update()

def animate():
    if state['turn']> 0:
        state['turn'] -=1
    spinner()
    ontimer(animate,20)

def flick():
    state['turn']+=10

setup(420,420,420,420)
hideturtle()
tracer(False)
width(20)
bgcolor('light blue')
onkey(flick,'space')
listen()
title("Fidget Spinner")
animate()
done()