from tkinter import *

def miles_to_km():
    try:
        miles = miles_input.get()
        km = float(miles) * 1.60934
        km_text_box.config(text= f"{km:.2f}")
    except ValueError:
        km_text_box.config(text="Invalid Input")
    except Exception as e:
        km_text_box.config(text=f"Error: {e}")
window = Tk()
window.title("Miles to Km converter")
window.minsize(width=300, height=300)
window.config()

text = Label(text="is equals to")
text.config(padx=20,pady=10)
text.grid(column=0, row=1)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)

km_text_box = Label(text="0")
km_text_box.grid(column=1, row=1)

km_text = Label(text="Km")
km_text.grid(column=2, row=1)
button = Button(text="Calculate", command=miles_to_km)
button.config(padx=10, pady=10)
button.grid(column=1, row=3)

window.mainloop()
# def add(*args):
#     print(type(args))
#     sum_of_n = 0
#     for n in args:
#         sum_of_n += n
#     return sum_of_n

# print(add(1,2,3,4,5,6))