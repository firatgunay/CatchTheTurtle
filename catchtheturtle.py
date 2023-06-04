# catch the turtle game

import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("catch the turtle")

FONT = ('Arial' , 25, 'normal')
grid_size = 10
turtle_list = []
score = 0
game_over =False
x_coordinates = [-20, -10 , 0, 10, 20]
y_coordinates = [20, 10, 0 -10, -20]

score_turtle = turtle.Turtle()
count_down_turtle = turtle.Turtle()

def setup_score_turtle():

    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.85
    score_turtle.setposition(0,y)
    score_turtle.color("dark blue")
    score_turtle.write(arg="score : 0", move=False, align="center", font=FONT)

def make_turle(x,y):
    t = turtle.Turtle()
    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"score : {score}", move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.setposition(x * grid_size , y * grid_size)
    turtle_list.append(t)


def setup_turtle():
    for i in x_coordinates:
        for k in y_coordinates:
            make_turle(i,k)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


def show_turtle_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtle_randomly,600)

def countdown(time):
    global game_over
    count_down_turtle.hideturtle()
    count_down_turtle.color("dark blue")
    count_down_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.85
    count_down_turtle.setposition(0, y-30)
    count_down_turtle.clear()

    if time > 0 :
        count_down_turtle.clear()
        count_down_turtle.write(arg=f"time : {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1) , 1000)
    else:
        game_over = True
        count_down_turtle.clear()
        hide_turtles()
        count_down_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)


def play_game():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtle()
    hide_turtles()
    show_turtle_randomly()
    countdown(20)
    turtle.tracer(1)

play_game()
turtle.mainloop()