from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self, position):
            new_seg = Turtle("square")
            new_seg.penup()
            new_seg.color("white")
            new_seg.goto(position)
            self.segments.append(new_seg)
            
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move_snake(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment -1].xcor()
            new_y = self.segments[segment -1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]