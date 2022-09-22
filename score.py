from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.scores = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto((0, 250))
        self.shapesize(2, 2)

    def add(self):
        self.clear()
        self.scores += 1
        self.color("white")
        self.write(f"score : {self.scores}", align="center", font=("courier", 24, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "bold"))