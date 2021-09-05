import turtle
import random


screen = turtle.Screen()
screen.setup(1000,1000)
screen.tracer(0,0)
turtle.hideturtle()
turtle.speed(0)
turtle.up()

A = (0,350)
B = (-300,-200)
C = (300,-200)
T = (A,B,C)
for F in T:
    turtle.goto(F)
    turtle.dot()


p = (random.uniform(-200,200),random.uniform(-200,200))
t = turtle.Turtle()
t.up()
t.hideturtle()

while(True):
    t.goto(p)
    t.dot(2)
    r = random.randrange(len(T))
    p = ((T[r][0]+p[0])/2,(T[r][1]+p[1])/2)
    t = turtle.Turtle()
    t.up()
    t.hideturtle()
    screen.update()


