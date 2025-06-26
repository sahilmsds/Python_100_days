from turtle import Turtle, Screen
import random 

sam = Turtle("circle")

colors = ["aquamarine", "blue2", "chocolate", "chartreuse", "darkorange", "firebrick", "magenta", "navy", "spring green", "yellow3"]
# def draw_shapes(turtle, num_of_sides):
#     angles = 360/num_of_sides
#     for _ in range(num_of_sides):
#         turtle.forward(100)
#         turtle.right(angles)

# for num in range(3, 11):
#     sam.color(random.choice(colors))
#     draw_shapes(sam, num)

screen = Screen()
screen.colormode(255)
# degrees = [0, 90, 180, 270]
# sam.pensize(15)
sam.speed("fastest")
def rgb_colors():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    random_colors = (r,g,b)
    return random_colors


# for _ in range(200):
#     sam.color(rgb_colors())
#     sam.setheading(random.choice(degrees))
#     sam.forward(50)
for _ in range(200):
    sam.color("white")
    sam.circle(0.1)
    
for _ in range(150):
    sam.color(rgb_colors())
    sam.circle(100)
    current_head = sam.heading()
    sam.setheading(current_head + 5)

screen.bgcolor("black")
screen.exitonclick()
