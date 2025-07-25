from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"Player1\n{self.l_score}", align= ALIGN,font=FONT)
        self.goto(100, 200)
        self.write(f"Player2\n{self.r_score}", align= ALIGN,font=FONT)
        
    def scoring_l(self):
        self.l_score += 1
        self.update_scoreboard()
    
    def scoring_r(self):
        self.r_score += 1
        self.update_scoreboard()
        