from turtle import Screen
from time import sleep

from paddle import P1Paddle, P2Paddle

# Instances:
screen = Screen()
player_1 = P1Paddle()
player_2 = P2Paddle()

# TODO Setting up game screen:
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# TODO Move paddles up and down:
screen.listen()

# Player 1:
screen.onkey(player_1.p1_move_up, "Up")
screen.onkey(player_1.p1_move_down, "Down")

# Player 2:
screen.onkey(player_2.p2_move_up, "w")
screen.onkey(player_2.p2_move_down, "s")

# Running the game:
game_on = True
while game_on:
    screen.update()


screen.exitonclick()
