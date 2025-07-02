from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

def quit_game():
    global game_is_on
    game_is_on = False

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")
screen.onkey(quit_game, "q")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    
        # Wall bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Paddle1 (right paddle) collision
    if ball.xcor() > 320 and ball.distance(paddle1) < 50:
        ball.bounce_x()

    # Paddle2 (left paddle) collision
    if ball.xcor() < -320 and ball.distance(paddle2) < 50:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        scoreboard.scoring_l()
        ball.reset_position()
    
    if ball.xcor() < -380:
        scoreboard.scoring_r()
        ball.reset_position()
screen.exitonclick()