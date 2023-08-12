from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

l_pos = (-380, 0)
r_pos = (380, 0)

l_paddle = Paddle(l_pos)
r_paddle = Paddle(r_pos)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collision_with_wall()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340 or ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.collision_with_paddle()
    if ball.xcor() > 380:
        ball.initial_place()
        scoreboard.l_scores()
    if ball.xcor() < -380:
        ball.initial_place()
        scoreboard.r_scores()
    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        game_on = False
        ball.game_end()



screen.exitonclick()



