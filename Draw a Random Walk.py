#Draw a Random Walk

import random
import turtle as t

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0,255)
    random_color = (r, g, b) #tuple
    return random_color
    
directions = [0, 90, 180, 270] #(0: east) (90: north) (180: south) (270: west)
tim.pensize(15)
tim.speed(0)

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
    

screen = Screen()
screen.exitonclick()
