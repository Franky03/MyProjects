from turtle import Turtle, Screen
import time
import random

START_POS=[(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20


class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        for position in START_POS:
            new_seg= Turtle()
            new_seg.penup()
            new_seg.color('white')
            new_seg.shape('square')
            new_seg.goto(position)
            new_seg.speed(1)
            segments.append(new_seg)

    def move_forward():
        screen.update()
        time.sleep(0.1)
        for seg_num in range(len(segments)-1, 0, -1):
            new_x= segments[seg_num-1].xcor()
            new_y= segments[seg_num-1].ycor()
            segments[seg_num].goto(new_x, new_y)
        
        segments[0].forward(10)
