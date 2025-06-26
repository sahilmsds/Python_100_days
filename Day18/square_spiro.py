# import turtle
# t = turtle.Turtle()                     #Definitions and Initializations
# screen = turtle.Screen()
# t.pensize(4)
# radius = 250                                    #Changeable to a number close to 250; Size of graphic
# number_of_points = 30                           #Changeable to a number close to 30; Count of points on invisible circumference
# list_of_points = []                             #Initial set of points on invisible circumference
# t.speed("fastest")
# def set_of_points(radius):                      #Procedure for identifying and listing points on invisible circumference                                            
#     for i in range(number_of_points):           #Loop to identify and list the indicated number_of_points 
#         new_point = t.position()                #Temporary assignment of current ordered pair to new_point   
#         list_of_points.append(new_point)        #Addition of latest new_point to list_of_points
#         t.circle(radius, 360 / number_of_points)         #Turtle movement to search for new point on the invisible circumference    
# t.penup()                               #Python_Graphic start of drawing procedure
# t.goto(0, -radius)
# set_of_points(radius)                           #Function call to identify & list points on circumference of circle w/ given radius
# t.pendown()
# for i in range(number_of_points):               #Loop to draw the basic pattern a number_of_points times
#     t.setheading(t.towards(0,0))                #Initialization of turtle direction toward (0, 0)
#     t.right(45)                                 #First angular rotation of turtle after pointing towards (0, 0)
#     t.color("blue")                             #Changeable color
#     t.forward(0.9 * radius)                     #First line of basic pattern
#     t.color("green")                            #Changeable color
#     t.circle(radius / 9, 120)                   #First arc of basic pattern
#     t.forward(1.1 * radius)                     #Second line of basic pattern
#     t.circle(radius / 7, 160)                   #Second arc of basic pattern
#     t.color("blue")                             #Changeable color
#     if i + 1 == number_of_points:               #Query to see if the basic pattern is the last one
#         t.goto(list_of_points[0])               #Drawing of last line for last basic pattern
#     else:
#         t.goto(list_of_points[i + 1])           #Drawing of last line for basic pattern that is not the last
# t.hideturtle()    
# screen.exitonclick()
from turtle import *

speed("fastest")
bgcolor("black")

colours = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(360):
    pencolor(colours[i%6])
    width(i / 250 + 1)
    forward(i)
    left(59)
    
hideturtle()
exitonclick()