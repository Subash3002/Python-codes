from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)


def draw_line(x, y):
    tom = Turtle()
    tom.hideturtle()
    tom.penup()
    tom.left(90)
    tom.goto(x=x, y=y)
    tom.pendown()
    tom.pensize(4)
    tom.forward(200)


# starting line
draw_line(-215, -90)
# finishing line
draw_line(240, -90)


colors = ["red", "orange", "green", "yellow", "blue", "purple"]
all_turtle = []
y_axis = -100
race_on = True
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    y_axis += 30
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis)
    all_turtle.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Guess which turtle win the race: ")
if not user_bet:
    race_on = False

while race_on:
    for current_turtle in all_turtle:
        if current_turtle.xcor() > 230:
            race_on = False
            winning_color = current_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win,{winning_color} turtle wins the race")
            else:
                print(f"You lose,{winning_color} turtle wins the race")
        current_turtle.forward(random.randint(0, 10))
