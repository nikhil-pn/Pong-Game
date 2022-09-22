from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(6, 1)
        self.goto(380, 0)

    def up(self):
        self.setheading(90)
        self.shapesize(1, 6)
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.shapesize(1, 6)
        self.forward(20)