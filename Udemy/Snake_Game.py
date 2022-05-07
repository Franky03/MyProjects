from turtle import Turtle, Screen
import random
import time

is_on= True
delay=0.1
score=0
highscore=0

screen= Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

food= Turtle()
food.penup()
colors= ["blue", "red", "green", "yellow"]
shapes= ["square", "triangle", "circle"]
food.color(random.choice(colors))
food.shape(random.choice(shapes))
x= random.randint(-280, 280)
y= random.randint(-280, 280)
food.goto(x, y)
food.shapesize(0.8)

start_pos=[(0, 0), (-20, 0), (-40, 0)]
segments=[]

for position in start_pos:
    snake= Turtle()
    snake.penup()
    snake.color('white')
    snake.shape('square')
    snake.goto(position)
    snake.speed(1)
    segments.append(snake)


pen= Turtle()
pen.pencolor("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 280)
# pen.write(f"Score : {score}  High Score : {highscore}", align= "center", font= ("candara", 12, "bold"))

def move_forward():
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x= segments[seg_num-1].xcor()
        new_y= segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    
    segments[0].forward(10)


def mlef():
    segments[0].left(90)

def mrig():
    segments[0].right(90)

screen.listen()

screen.onkey(key='Right', fun= mrig)
screen.onkey(key='Left', fun= mlef)


x= random.randint(-280, 280)
y= random.randint(-280, 280)
food.goto(x, y)


while is_on:
    _= 1
    segments[0].speed(_)
    move_forward()
    if snake.xcor()>= 288 or snake.xcor() <= -288:
        is_on=False
        # for segment in segments:
        #     segment.goto(1000,1000)
        # segments.clear()
    elif snake.ycor() >=298 or snake.ycor() <=-298:
        is_on= False
        # for segment in segments:
        #     segment.goto(1000,1000)
        # segments.clear()

    if snake.distance(food)< 20:
        x= random.randint(-280, 280)
        y= random.randint(-280, 280)
        food.goto(x, y)
        food.color(random.choice(colors))
        food.shape(random.choice(shapes))
        new_seg= Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color('orange')
        new_seg.penup()
        segments.append(new_seg)
        score+=1
        _ +=1
        delay -=0.001
        if score>highscore:
            highscore= score

        pen.clear()
        pen.write(f"Score : {score}  High Score : {highscore}", align= "center", font= ("candara", 12, "bold"))


        

screen.exitonclick()
