from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,275)
        self.write(f"score: {self.score}",align=ALIGN,font=FONT)
        self.hideturtle()
        
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!",align=ALIGN,font=FONT)
        self.goto(0, -30)
        self.write(f"Your Final score is {self.score}", align=ALIGN, font=FONT)
    def scoring(self):
        self.score +=1
        self.clear()
        self.write(f"score: {self.score}",align=ALIGN,font=FONT)