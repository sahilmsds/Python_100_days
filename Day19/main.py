from turtle import Turtle, Screen
import random
colors = ["red", "green", "orange", "pink", "blue", "purple"]
y_coordinates = [-80, -50, -20, 10, 40, 70]
turtles_list = []
def gen_turtle(turtles_list, colors):
    for index in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[index])
        new_turtle.goto(x=-230, y=y_coordinates[index])
        turtles_list.append(new_turtle)
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Turtle Race",prompt="Make your bet:")   
if user_bet:
    is_game = True
gen_turtle(turtles_list=turtles_list, colors=colors) 
while is_game: 
    
    for turtles in turtles_list:
        if turtles.xcor()>215:
            win_color = turtles.pencolor()
            if user_bet == win_color:
                print(f"Winner: {win_color}")
            else:
                print(f"You lose the bet. The winner of the race is {win_color} turtle.")
            is_game = False
        turtles.forward(random.randint(0,10))
        
        
screen.exitonclick()