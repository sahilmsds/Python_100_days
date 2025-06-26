from turtle import Turtle, Screen
import random

rgb_cols = []
colors = [(248, 247, 240), (239, 250, 245), (251, 241, 247), (237, 243, 250), (235, 226, 87), (210, 161, 109), (113, 177, 212), (201, 5, 68), (230, 52, 128), (196, 77, 19), (217, 133, 177), (193, 164, 15), (34, 106, 166), (11, 21, 62), (32, 189, 114), (232, 224, 4), (18, 28, 171), (122, 188, 161), (204, 32, 127), (233, 165, 197), (14, 183, 211), (10, 45, 24), (38, 132, 72), (45, 15, 10), (105, 92, 210), (139, 219, 203), (185, 13, 6), (135, 218, 232), (229, 73, 45), (169, 180, 229), (79, 7, 25), (12, 97, 49), (233, 173, 163), (253, 5, 47), (22, 36, 246), (13, 85, 101), (58, 82, 16), (255, 8, 4), (47, 249, 96)]

sam = Turtle("circle")

screen = Screen()
screen.colormode(255)
sam.speed("fastest")
sam.penup()
sam.setheading(225)
sam.forward(300)
sam.setheading(0)

n_of_dot_count = 100

for dot_count in range(1, n_of_dot_count + 1):
    sam.dot(20, random.choice(colors))
    sam.forward(50)
    
    if dot_count%10 == 0:
        sam.setheading(90)
        sam.forward(50)
        sam.setheading(180)
        sam.forward(500)
        sam.setheading(0)

sam.hideturtle()
screen.exitonclick()