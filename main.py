import tkinter
from tkinter import Canvas

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global marks
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    top_label.config(text="Timer")
    marks = ""
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        top_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        top_label.config(text="Break", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        top_label.config(text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    global marks
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            marks += "✔️"
            checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)
top_label = tkinter.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
top_label.grid(row=0, column=1)
start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)
reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)
checkmark = tkinter.Label(fg=GREEN, bg=YELLOW)
checkmark.grid(row=2, column=1)
checkmark.config(padx=0, pady=25)



window.mainloop()