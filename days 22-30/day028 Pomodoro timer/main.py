from tkinter import *
import time
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

is_on = True
rounds = 0
exit_timer = False


def timer(sleep):
    print(sleep)
    time.sleep(sleep)


def exit_b():
    exit_timer = True


def reset_b():
    pass


# while is_on:
#     timer(WORK_MIN)

#     rounds += 1

#     if rounds < 4:
#         timer(SHORT_BREAK_MIN)
#     elif rounds == 4:
#         timer(LONG_BREAK_MIN)
#         rounds = 0

#     if exit_timer:
#         is_on = False


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    countdown(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, countdown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=30, pady=30, bg=YELLOW)

timer_label = Label(text="TIMER", font=(
    FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(
    file="/Users/Daniel/Documents/Phyton Bootcamp/days 22-30/day028 Pomodoro timer/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

button_exit = Button(text="EXIT", command=exit_b, highlightthickness=0)
button_exit.grid(row=2, column=0)

button_reset = Button(text="RESET", command=reset_b, highlightthickness=0)
button_reset.grid(row=2, column=2)

timer_label = Label(text="✔", font=(
    FONT_NAME, 18, "bold"), bg=YELLOW, fg=PINK)
timer_label.grid(row=3, column=1)

start_timer()

window.mainloop()
