from turtle import Screen, setheading, color, begin_fill, left, forward, right, end_fill, circle, fillcolor
from helpers import restore_state_when_finished
import time

def small_circle(size, color_name):
    color(color_name)
    begin_fill()
    circle(size)
    end_fill()

def pac_man():
    fillcolor("yellow")
    left(150)
    begin_fill()
    circle(50,270)
    left(90)
    forward(50)
    right(90)
    forward(50)
    end_fill()
    right(60)

def moving_pacman(sleeptime, screen):
        penup()
        forward(5)
        pendown()
        pac_man()
        right(60)
        screen.update()
        time.sleep(sleeptime)
        clear()
        
   

    
    
    