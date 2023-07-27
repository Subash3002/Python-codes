from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 1
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.count += 1
        # if self.count % 5 ==0:
        #     self.color("red")
        #     self.shapesize(stretch_len=1, stretch_wid=1)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    # def big_food(self):
    #     random_x = random.randint(-280, 280)
    #     random_y = random.randint(-280, 280)
    #
    #     self.goto(random_x, random_y)






