from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz= quizbrain
        self.window = Tk()
        self.window.title("Trivia Quiz")
        self.window.config(padx=20 ,pady=20,bg=THEME_COLOR)
        
        self.score_label = Label(text="Score : 0", fg="white",bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)
        
        self.canvas = Canvas(width=500,height=450,bg="white")
        self.question_text = self.canvas.create_text(250,
                                                     225,
                                                     width=280,
                                                     text="some_question",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 25, "normal"))       
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0,command=self.pressed_False)
        self.false_button.grid(column=0, row=2)
        
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0,command=self.pressed_True)
        self.true_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
           
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text="End of the Quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.window.after(3000, self.window.destroy)
        
    def pressed_True(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def pressed_False(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)