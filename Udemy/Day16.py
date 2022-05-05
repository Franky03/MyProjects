import turtle as tl
import random

timmy= tl.Turtle()
tom= tl.Turtle()
tom.shape("turtle")
tom.color("darkblue")
tom.hideturtle()
timmy.shape("arrow")
timmy.color("darkblue")
#Dashed Line

# for c in range(4):
#     for _ in range(10):
#         timmy.forward(5)
#         timmy.penup()
#         timmy.forward(5)
#         timmy.pendown()
#     timmy.right(90)
timmy.speed(4)
colors=['darkred', 'darkblue', 'chartreuse', 'yellow', 'purple', 'pink', 'deep sky blue', 'magenta', 'blue']
def shap(numS):
    for i in range(numS):
        timmy.forward(100)
        timmy.left(360/numS)

for _ in range(3, 11):
    col= random.choice(colors)
    shap(_)
    timmy.color(col)
    colors.remove(col)

#Square
# for c in range(4):
#     timmy.forward(100)
#     timmy.left(90)

screen= tl.Screen()
screen.exitonclick()

