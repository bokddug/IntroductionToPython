"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and JaeJung Hyun.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(50)
 
JA= rg.SimpleTurtle('turtle')
JJ= rg.SimpleTurtle('turtle')

JA.pen =rg.Pen('blue', 4)
JA.speed =10
size =200
for k in range(5):
    JA.draw_square(200)
    JA.pen_up()
    JA.left(30)
    JA.forward(80)
    JA.right(30)
    JA.pen_down()
    size= size -5

JJ.pen =rg.Pen('red', 10)
JJ.speed = 10
JJ.draw_circle(50)
JJ.forward(50)
JJ.left(50)
JJ.backward(100)