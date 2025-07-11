from tkinter import *
import pandas as pd
import random as rn
BACKGROUND_COLOR = "#B1DDC6"
choosen = {}
diction = {}
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    origional_data = pd.read_csv("data/french_words.csv")
    diction = origional_data.to_dict(orient="records")
else:
    diction = data.to_dict(orient="records")

def next_card():
    global choosen, flip_timer
    choosen = rn.choice(diction)
    window.after_cancel(flip_timer)
    answer = choosen["French"]
    canvas.itemconfig(canvas_title, text="French",fill="black")
    canvas.itemconfig(canvas_text, text=answer,fill="black")
    canvas.itemconfig(front_card, image=card_front_img)
    flip_timer = window.after(3000,func=flip_card)
    
def flip_card():
    global choosen
    guess = choosen["English"]
    canvas.itemconfig(canvas_title, text="English",fill="white")
    canvas.itemconfig(canvas_text, text=guess,fill="white")
    canvas.itemconfig(front_card, image=new_front_img)

def is_known():
    # global choosen
    diction.remove(choosen)
    df =pd.DataFrame(diction)
    df.to_csv("data/words_to_learn.csv",index=False)
    next_card()

window = Tk()
window.title("Learn French")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
# window.geometry("900x626")
flip_timer = window.after(3000,func=flip_card)

canvas=Canvas(width=800, height=526,highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
new_front_img = PhotoImage(file="images/card_back.png")

front_card=canvas.create_image(400,263,image=card_front_img)

canvas_title = canvas.create_text(400,150,text="", font=("Ariel", 20, "bold"))
canvas_text = canvas.create_text(400,263,text="", font=("Ariel", 40, "bold"))

canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0,row=0,columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
unknown_botton= Button(image=wrong_img,highlightthickness=0,command=next_card)
unknown_botton.grid(column=0,row=1)

correct_img = PhotoImage(file="images/right.png")
correct_botton = Button(image=correct_img,highlightthickness=0,command=is_known)
correct_botton.grid(column=1,row=1)

next_card()
window.mainloop()
