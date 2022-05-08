from turtle import Turtle, Screen
import time
import random

START_POS=[(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP= 90
DOWN= 270
LEFT= 180
RIGHT= 0
game_is_on= True
score=0
highscore=0
life=3

screen= Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

#SNAKE 

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments=[]
        self.create_snake()
        self.head= self.segments[0]
    def create_snake(self):
        for position in START_POS:
            snake= Turtle()
            snake.penup()
            snake.color('white')
            snake.shape('square')
            snake.goto(position)
            snake.speed(1)
            self.segments.append(snake)
    
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x= self.segments[seg_num-1].xcor()
            new_y= self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        self.head.forward(MOVE_DISTANCE)
    def mlef(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def mrig(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def mup(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def mdown(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def tail(self):
        new_seg= Turtle()
        new_seg.shape("square")
        new_seg.color('orange')
        new_seg.penup()
        new_seg.speed("fastest")
        self.segments.append(new_seg)
    def restart(self):
        global life, score
        life-=1
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        score=0
        time.sleep(1)
        self.__init__()
        self.head.goto(0,0)

snake= Snake()
screen.listen()
screen.onkey(key= 'Up', fun= snake.mup)
screen.onkey(key='Down', fun= snake.mdown)
screen.onkey(key='Right', fun= snake.mrig)
screen.onkey(key='Left', fun=snake.mlef)

#FOOD
class Food(Turtle):
    def __init__(self):
        super().__init__()
    
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x= random.randint(-280, 280)
        y= random.randint(-280, 280)
        self.goto(x,y)

        colors= ["blue", "red", "green", "yellow"]
        shapes= ["square", "triangle", "circle"]
        self.new_col= random.choice(colors)
        self.new_shape= random.choice(shapes)
        self.color(self.new_col)
        self.shape(self.new_shape)

food= Food()

#PEN
class Pen(Turtle):
    def __init__(self):
        super().__init__()
        global score
        global highscore
        global life
        self.pencolor('white')
        self.penup()
        self.hideturtle()
        self.refresh()

        
    def refresh(self):
        self.clear()    
        self.goto(0,280)
        self.write(f"Score : {score}  High Score : {highscore}", align= "center", font= ("candara", 12, "bold"))
        self.goto(280,280)
        self.write(f'Life: {life}', align='right', font= ("candara", 12, "bold"))

pen= Pen()

#GAME

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.xcor()>= 288 or snake.head.xcor() <= -288 or snake.head.ycor() >=298 or snake.head.ycor() <=-298:
        snake.restart()
        pen.refresh()
    
    if snake.head.distance(food)<15:
        snake.tail()
        food.refresh()
        score+=1
        highscore +=1
        pen.refresh() 
    
    if life==0:
        game_is_on=False

         

screen.exitonclick()
