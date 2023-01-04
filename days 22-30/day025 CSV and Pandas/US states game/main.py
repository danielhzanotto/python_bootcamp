import turtle
import pandas

screen = turtle.Screen()
screen.title("US Names Game")
image = "/Users/Daniel/Documents/Phyton Bootcamp/days 22-30/day025 CSV and Pandas/US states game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(
    "days 22-30/day025 CSV and Pandas/US states game/50_states.csv")


def print_state(x, y, state):
    tim = turtle.Turtle()
    tim.hideturtle()
    tim.penup()
    tim.goto(x, y)
    tim.write(state)


answers = {
    "states": [],
    "x": [],
    "y": [],
}

is_on = True
while is_on:
    answer_state = screen.textinput(
        title="Guess The State", prompt="Write a state name")
    for state in data["state"]:
        if answer_state.title() == state:
            get_state = data[data["state"] == answer_state.title()]
            x_cor = get_state["x"][get_state.index].item()
            y_cor = get_state["y"][get_state.index].item()
            state_name = get_state["state"][get_state.index].item()
            answers["states"].append(state_name)
            answers["x"].append(x_cor)
            answers["y"].append(y_cor)
            print_state(x_cor, y_cor, state_name)

    if answer_state.title() == "Exit":
        is_on = False
        score = len(answers["states"])
        print(f"Your score is {score}")

    if len(answers["states"]) == len(data["state"]):
        print("Congratuations, you win!")


screen.exitonclick()
