from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("D:\\100 days bootcamp\\Day20_Day21\\data.txt") as dt:
            self.high_score = int(dt.read())
        self.color("white")
        self.penup()
        self.goto(0,275)
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score}, High Score: {self.high_score}",align=ALIGN,font=FONT)
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("D:\\100 days bootcamp\\Day20_Day21\\data.txt", mode='w') as dt:
                dt.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    

    def scoring(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()