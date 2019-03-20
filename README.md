# Ball-world
python
ballworld.py

This program consists of a class named Ball, which has 2 further subclasses named BreathingBall
and WarpBall. Ball consists of a constructor and the following method functions: setPos(), setColor(),
setSize(), update(), and move(). BreathingBall and WarpBall import the constructor from their
superclass. BreathingBall also imports update() from its super class and then overrides it to perform
some additional functions. WarpBall doesn’t import update from its superclass and updates with its
particular method. The purpose of this program is to make a simulation of balls which are walking in a
window in a random fashion.

Ball’s constructor here takes no external input and randomly generates all the instance and
other variables to be later used in the program. It also sets up a turtle as a circle for given parameters.
setPos() sets a circle to particular coordinates within a window. setColor() sets a circle to a given color.
setSize() uses sets a circle size to a given radius. update() makes sure that a circle’s given coordinates
don’t go out of the window. Then it calls the setColor() to change a circle’s color. move() changes a
circle’s coordinates for a given velocity and sets the circle to the new coordinates by calling the setPos()
function.

BreathingBall’s constructor, as mentioned before, imports Ball’s constructor. It also randomly
generates an instance variable called step which is later used in its update() method. The update()
method uses a sine wave to help generate a radius for the circles. The step variable is used here to alter
the radius of these circles.

WarpBall makes balls which when hit one side of the turtle window, appear at exactly the other
side without any change in speed or direction of the ball. It does this by using comparison operators and
allotting the min x or y coordinate to the balls at the maximum and vice versa.
