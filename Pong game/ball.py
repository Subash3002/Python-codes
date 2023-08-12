from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.08

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def collision_with_wall(self):
        self.y_move *= -1

    def collision_with_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def initial_place(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.collision_with_paddle()

    def game_end(self):
        self.write("Game over", align="center", font=("Courier", 80, "normal"))


