from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

player_1 = Score()
player_2 = Score()

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_r = Paddle()
paddle_l = Paddle()
paddle_l.goto(-380, 0)

ball = Ball()
ball.move()

screen.listen()
screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")

screen.onkeypress(paddle_l.up, "w")
screen.onkeypress(paddle_l.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_game()
        player_1.goto(-300, 250)
        player_1.add()

    if ball.xcor() < -400:
        ball.reset_game()
        player_2.goto(300,250)
        player_2.add()

screen.exitonclick()