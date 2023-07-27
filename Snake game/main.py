from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scorecard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scorecard.increase_score()

    if snake.head.xcor() > 290:
        snake.wall(-290, snake.head.ycor())

    if snake.head.xcor() < -290:
        snake.wall(290, snake.head.ycor())

    if snake.head.ycor() > 290:
        snake.wall(snake.head.xcor(), -290)

    if snake.head.ycor() < -290:
        snake.wall(snake.head.xcor(), 290)

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            #game_on = False
            scorecard.reset_score()
            snake.reset()
            # user = screen.textinput(prompt="Continue?", title="c")
            # if user == "y":



screen.exitonclick()