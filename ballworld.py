import turtle
from ball import *

def main():
    simTurtle = turtle.Turtle()
    turtle.setworldcoordinates(0, 0, 1, 1)
    turtle.tracer(50)
    simTurtle.hideturtle()

    ballList = []
    for i in range(5):
        ballList.append(Ball())
        ballList.append(BreathingBall())
        ballList.append(WarpBall())

    while True:
        for b in ballList:
            b.update()
            b.move()
        
        
main()