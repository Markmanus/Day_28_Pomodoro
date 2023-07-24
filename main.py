from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
def start_timer():
    count_down((WORK_MIN*60)-1)

def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(time_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=220, height=225 ,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103,113,image=tomato_img)
time_text = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

text = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"bold"))
text.grid(column=1,row=0)

button_start = Button(text="Start",highlightthickness=0 ,command=start_timer)
button_start.grid(column=0,row=2)

button_reset = Button(text="Reset",highlightthickness=0)
button_reset.grid(column=2,row=2)

check_mark = Label(text="✔",fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))



window.mainloop()
