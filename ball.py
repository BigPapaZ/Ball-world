#######################
# ball.py
# Zaigham
# Defines a Ball Class and some further sub-classes
#######################


import turtle
import random
import math

class Ball:

    #Constructor
    def __init__(self):
        self.x, self.y=random.random(),random.random()
        self.__xVel, self.__yVel=random.random()*0.01-.005, random.random()*0.01-.005
        self.__size=random.random()+1
        self.__rColor, self.__gColor, self.__bColor=random.random(),random.random(),random.random()

        self.bTurtle=turtle.Turtle()
        self.bTurtle.shape("circle")
        self.bTurtle.resizemode("user")
        self.bTurtle.turtlesize()
        self.bTurtle.penup()


    def setPos(self, x, y):
        '''
        Sets the position of the ball
        Input: Ball(as self) and Coordinates
        Output: None (although turtle is set to a new position)
        '''
        self.bTurtle.setpos(x,y)

    def setColor(self,r,g,b):
        '''
        Sets the RGB level of the ball
        Input: Ball(as self) and the rgb levels
        Output: None (although turtle's colour is changed)
        '''
        self.bTurtle.color((r,g,b))

    def setSize(self, size):
        '''
        Sets the size of the ball
        Input: Ball(as self) and the radius of the ball
        Output: None (although the turtle's size is changed)
        '''
        self.bTurtle.turtlesize(size)

    def update(self):
        '''
        Makes sure that the balls stay within the screen and changes their colour
        Input: Ball
        Output: None (although ball's velocity and rgb are changed
        '''


        if self.x<0 or self.x>1:
            self.__xVel*=-1
        if self.y<0 or self.y>1:
            self.__yVel*=-1

        self.setColor(self.__rColor,self.__gColor,self.__bColor)

    def move(self):
        '''
        Changes a ball's position
        Input: Ball
        Output: None (although ball's position is changed)
        '''

        self.x+=self.__xVel
        self.y+=self.__yVel
        self.setPos(self.x, self.y)



class BreathingBall(Ball):
    '''
    Makes a ball whose size keeps changing
    '''
    def __init__(self):
        super().__init__()
        self.__step=random.randint(0,120)


    #Changing the radius with time
    def update(self):
        super().update()
        self.setSize(3*abs(math.sin(self.__step/20))+.5)
        self.__step+=1



class WarpBall(Ball):
    '''
    Makes a ball which can awrp across the screen when it hits the boundries
    '''
    def __init__(self):
        super().__init__()

    #Making sure that the ball doesn't go out of the boundries of the window
    def update(self):
        if self.x>1:
            self.x=0
        if self.y>1:
            self.y=0
        if self.x<0:
            self.x=1
        if self.y<0:
            self.y=1