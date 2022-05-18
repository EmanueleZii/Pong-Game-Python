from turtle import Screen  # importa la libreria grafica turtle
# importa le classi custom
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time  # importa il frame

#impostazioni dello schermo
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")

screen.tracer(0) #toglie le animazioni

#le posizioni dei due paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()

#comandi dei paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball() #instazia la palla al centro
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # far rilevare la collisione alla palla con il muro
    if ball.ycor() > 300 or ball.ycor() < -300:  # bisogno di rimbalzo
        ball.bounce_y()

    # rilevare le collisioni con i paddle left e right
    if ball.distance(r_paddle) < 50 and ball.xcor() > 348:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() > -348:
        ball.bounce_x()

    # rilevare se il right paddle manca la palla
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # rilevare se il left paddle manca la palla
    if ball.xcor() < 380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
