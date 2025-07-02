from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGN = "left"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 265)
        self.write(f"Level {self.level}", align=ALIGN, font=FONT)
        
    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level {self.level}", align=ALIGN, font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)