from turtle import Screen
from time import sleep
from random import randint

from paddle import P1Paddle, P2Paddle
from ball import Ball

# Instances:
screen = Screen()
player_1 = P1Paddle()
player_2 = P2Paddle()
ball = Ball()

# TODO Setting up game screen:
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# TODO Move paddles up and down:
screen.listen()

# Player 1:
screen.onkey(player_1.move_up, "Up")
screen.onkey(player_1.move_down, "Down")

# Player 2:
screen.onkey(player_2.move_up, "w")
screen.onkey(player_2.move_down, "s")

# Running the game:
game_on = True
while game_on:
    screen.update()
    sleep(0.1)
    ball.ball_move()

    # Detect wall collision:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with Player 1:
    if ball.distance(player_1) < 50 and ball.xcor() == 340:
        ball.bounce_x()
        print("P1 touches the ball!")

    if ball.distance(player_2) < 50 and ball.xcor() == -340:
        print("P2 touches the ball!")
        ball.bounce_x()

    if ball.xcor() > 360:
        print("P1 loses a ball!")
        sleep(1)
        ball.out_of_bounds()

    if ball.xcor() < -360:
        print("P2 loses a ball!")
        sleep(1)
        ball.out_of_bounds()


screen.exitonclick()
