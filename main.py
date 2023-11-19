import turtle
import pandas

# Create a Turtle graphics screen with a title.
screen = turtle.Screen()
screen.title("India States Game")

# Load the background image for the game.
image = "images/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the data containing Indian states and union territories.
data = pandas.read_csv("data/28_states_8_union territories.csv")

# Create a list of all the Indian states.
all_states = data.state.to_list()

# Create an empty list to store the states that have been guessed.
guessed_states = []

# Main game loop: Continue until all states have been guessed or the user exits.
while len(guessed_states) < 36:
    # Ask the user for input and title of the input box shows the progress.
    answer_state = screen.textinput(title=f" {len(guessed_states)}/36 States correct",
                                    prompt="What's another state's name? ").title()

    # Check if the user wants to exit the game.
    if answer_state == "Exit":
        # Find the missing states and store them in a new CSV file.
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Check if the user's input matches any of the Indian states.
    if answer_state in all_states:
        # If the input matches, add it to the guessed states and display it on the map.
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


        # if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # new_data = pandas.DataFrame(missing_states)
        # new_data.to_csv("states_to_learn.csv")
        # break