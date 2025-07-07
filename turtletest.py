import turtle
from turtle import *

screen = turtle.Screen()
#screen.setup(width=1000, height=1000)
screen.bgcolor("lightblue")
turtle.pensize(5)

def circle_flower(radius=100):
  circumference = 2 * 3.14 * 100
  step = circumference / 360
  for i in range(90):
    forward(step)
    left(1)
    color('orange')

def petal():
  circle_flower()
  left(90)
  circle_flower()
  left(60)


for i in range(12):
  petal()


def circle(radius=150):
    for i in range(2):
        a = radius + (i * 20)
        up()
        home()
        right(90)
        forward(a)
        left(90)
        down()
        color('indigo')
        circumference = 2 * 3.14 * a
        step = circumference / 360
        for i in range(360):
            forward(step)
            left(1)
circle()

# for right side down
up()
home()
down()
for i in range(24):
    a = 90 - i * 15
    b = i * 15
    color('red')
    up()
    home()
    right(a)
    forward(170)
    left(0)
    down()
    forward(100)
    right(45)
    petal()

for i in range(48):
    a = 90 - i *7.5
    b = i*7.5
    color('black')
    up()
    home()
    right(a)
    forward(170)
    left(0)
    down()
    forward(50)
    for i in range(4):
        right(45)
        forward(5)
    forward(45)


turtle.done()
