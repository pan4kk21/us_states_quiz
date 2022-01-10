import turtle
import pandas

my_screen = turtle.Screen()
my_screen.title("US States Quiz")
image = "blank_states_img.gif"
my_screen.addshape(image)
my_screen.setup(width=725, height=500)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states_list = data.state.to_list()

while len(all_states_list) != 0:
    state_guess = my_screen.textinput(title=f"Guessed states: {50 - len(all_states_list)}/50",
                                      prompt="Make your guess:").title()
    if state_guess == "Exit":
        break
    if state_guess in all_states_list:
        all_states_list.remove(state_guess)
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        state_info = data[data.state == state_guess]
        new_turtle.goto(x=int(state_info.x), y=int(state_info.y))
        new_turtle.write(arg=state_guess)

pandas.DataFrame(all_states_list).to_csv("unguessed_states")


