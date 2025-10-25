import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown', 'cyan', 'magenta']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... try again!")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number must be in between 2-10")


def create_turtles(colors):
    turtles = []
    for i, color in enumerate(colors):
        racer = turtle.Turtle()

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle Racing')

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
print(colors)

