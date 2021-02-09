import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Quiz")

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
turtle_text = turtle.Turtle()  # Text turtle
turtle_text.penup()
turtle_text.hideturtle()


# def get_mouse_click_coor(x,y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv('50_states.csv')
states_list = []

while len(states_list) < 50:

    answer = (screen.textinput(title=f'{len(states_list)} out of 50 states correct', prompt='Enter a name of a state')).title()
    states_list.append(answer)
    for index, rows in data.iterrows():
        if rows.state == answer:         # Find row containing the suggested state
            turtle_text.setpos(rows.x, rows.y)

            turtle_text.write(answer)

turtle.mainloop()