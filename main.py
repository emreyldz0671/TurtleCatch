import turtle
import random

board_emre = turtle.Screen()
board_emre.bgcolor("light green")
board_emre.title("Kaplumbagayi Yakala")
FONT = ('Arial',15,'bold')
score = 0
game_over = False

#turtle list
turtle_list = []

#Score Turtle
score_turtle = turtle.Turtle()

#Countdown Turtle
countdown_turtle = turtle.Turtle()

#make turtle properties
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]
grid_size = 10

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = board_emre.window_height() /2
    y = top_height * 0.9
    score_turtle.setpos(0,y)
    score_turtle.write(arg="Score 0",move=False,align="center",font=FONT)

def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score:{score}",move=False,align="center",font=FONT)
        #print(x,y)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2)
    t.color("blue")
    t.goto(x * grid_size,y * grid_size)
    turtle_list.append(t)

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursive function
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        board_emre.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()

    top_height = board_emre.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.setpos(0, y - 30)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        board_emre.ontimer(lambda: countdown(time-1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)

def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)

start_game_up()
turtle.mainloop()