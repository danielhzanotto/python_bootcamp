from tkinter import *
import time
import math


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


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    timer_label["text"] = "TIMER"
    timer_check["text"] = ""
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label["text"] = "BREAK"
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label["text"] = "BREAK"
    else:
        countdown(work_sec)
        timer_label["text"] = "WORK"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        if reps % 2 != 0:
            timer_check["text"] += "✔"
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=30, pady=30, bg=YELLOW)

timer_label = Label(text="TIMER", font=(
    FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(
    file="days 22-30/day028 Pomodoro timer/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

button_exit = Button(text="START", command=start_timer, highlightthickness=0)
button_exit.grid(row=2, column=0)

button_reset = Button(text="RESET", command=reset_timer, highlightthickness=0)
button_reset.grid(row=2, column=2)

timer_check = Label(font=(
    FONT_NAME, 18, "bold"), bg=YELLOW, fg=PINK)
timer_check.grid(row=3, column=1)

window.mainloop()
