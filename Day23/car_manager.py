from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_cars(self):
        if random.randint(1,6) == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_ycor = random.randint(-250, 250)
            new_car.goto(300, new_ycor)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT 