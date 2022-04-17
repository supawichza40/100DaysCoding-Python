from turtle import Screen,Turtle
import pandas
def find_state(user_answer):

    result = states_df[states_df["state"] == str(user_answer).title()]
    if not result.empty:
        return result
    else:
        return ""

def write_name_on_window(found_state):
    state_writer.goto(x=float(found_state["x"]), y=float(found_state["y"]))
    state_writer.write(arg=result["state"].values[0], move=True, align="center")
def create_new_file_and_delete_exist_info():

    with open("answered_state.txt","w") as answered_state:
        answered_state.write("")
create_new_file_and_delete_exist_info()
screen = Screen()
map = Turtle()
state_writer = Turtle()
screen.addshape("blank_states_img.gif")
map.shape("blank_states_img.gif")

states_df = pandas.read_csv("50_states.csv")
number_state = 0
answered_state = []
while(number_state<=55):
    user_answer = screen.textinput("state_name","What's another state name?")
    if user_answer == "exit":
        break
    result = find_state(user_answer)
    if(str(result)!=""):
        if(user_answer.title() not in answered_state):
            answered_state.append(user_answer.title())
        write_name_on_window(result)

print(f"You have answered {len(answered_state)} out of 55 states")
with open("answered_state.txt",mode="w") as file:
        for state in answered_state:
            file.write(f"{state}\n")

