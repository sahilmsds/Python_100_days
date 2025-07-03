from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def draw_game_border():
    border = Turtle()
    border.hideturtle()
    border.penup()
    border.pencolor("white")
    border.speed("fastest")
    border.goto(-280, 280)
    border.pendown()
    for _ in range(4):
        border.forward(560 if _ % 2 == 0 else 560)
        border.right(90)

screen = Screen()
screen.setup(width=600, height=650)
screen.title("Nokia 3310 Relive")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
draw_game_border()
snake.create_snake()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    
    # Collision with food
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        scoreboard.scoring()
    
    # collision with wall
    if (snake.head.xcor()> 279 or snake.head.xcor()< -279 or snake.head.ycor() > 279 or snake.head.ycor() < -279):
        scoreboard.reset()
        snake.reset()
        
    # Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
screen.exitonclick()