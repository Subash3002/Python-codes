from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.score = 0
        with open("highscore.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.printing_score()

    def printing_score(self):
        self.clear()
        self.write(f"Score : {self.score} Highscore : {self.highscore}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.printing_score()

    # def high_score(self):
    #     self.score += 5
    #     self.clear()
    #     self.printing_score()
    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.printing_score()

    # def game_end(self):
    #
    #     self.goto(0, 0)
    #
    #
    #     self.write("Game Over", align="center", font=("Arial", 24, "normal"))



