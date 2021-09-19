# import Shapeline so to form a star I just create 2 lines
from PositionalVectors import Vector2
import ShapeLine
# importing shapes to add the stars directly into the array, this file should never create any objects, but other files that call this will create objects
import Shapes
# importing random
import random


# creating the star class
class star():

    # constructor, takes in one linePosition, then takes in another
    def __init__(self, line1StartPos, line1EndPos, line2StartPos, line2EndPos, color = [255,255,255], width = 2):
        
        # creating the first line
        self.line1 = ShapeLine.Line(line1StartPos, line1EndPos, color, width)
    
        # creating the second line
        self.line2 = ShapeLine.Line(line2StartPos, line2EndPos, color, width) 

        # debug
        
        # appending the lines into the array
        Shapes.lines.append(self.line1)
        Shapes.lines.append(self.line2)

        print("Line :", Shapes.lines[0].One.x, Shapes.lines[0].One.y, Shapes.lines[0].Two.x, Shapes.lines[0].Two.x)


# creating the function to create a random star
def createStar():
    # creating points, using random number to determine 1, adding 20 to the first
    point1 = random.randrange(1,1200)
    point2 = random.randrange(1,600)

    # transforming the points into a vector
    a = Vector2(point1, point2)
    # creating the first line, going at a slope of 1
    b = Vector2(point1+5, point2+5)

    # creating the 2nd line starting position, adding 20 to the x of a, using point2
    c = Vector2(point1+5, point2)

    # creating the 2nd line ending position, instead of adding 20 to the x we add 20 to y to form a slope of 20
    d = Vector2(point1, point2+5)

    # creaing the star
    star(a,b,c,d)
    
    print(a.x, a.x, b.x, b.y)
    

       
    
    
   




# creating the star function, it will just add 2 lines
