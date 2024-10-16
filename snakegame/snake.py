from turtle import Turtle,Screen
import time

screen =Screen() 
POSITION = [(0,0),(-20,0),(-40,0)] # This is the List of Tuples having position of first the segment of snake body where they get started.
MOVE_BY_STEPS = 20 # Constant variable.   For snake body how much forward in each step

UP = 90         # Constant variable  for controling the snake using button (Left arrow key , Right arrow key ,UP arrow key, down arrow key)
DOWN = 270      # Constant variable
LEFT = 180      # Constant variable     
RIGHT = 0       # Constant variable

class Snake():
    """This is snake class Formal parameters => 'NONE' 
        it craetes the snake object and make the body of snake with first three segment"""
    def __init__(self):
        self.segment = []
        self.Create_Snake()
        self.head = self.segment[0]

    def Create_Snake(self):
        """Create_Snake is a function which create a snake body with the help of function 'add_segment'."""
        for pos in POSITION:
            self.add_segment(pos)

    def add_segment(self,pos):
            """add_segment is a function that helps to add a new segment when it ear food for the first time it allredy creates three segment for calling in Create_Sanke function """
            new_segment = Turtle(shape="square")
            new_segment.color("green")
            new_segment.penup()
            new_segment.goto(pos)
            self.segment.append(new_segment)
    def extend(self):
        # for add new segment when it eat food.
        self.add_segment(self.segment[-1].position())
    def Move(self):
        for seg in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[seg-1].xcor()
            new_y = self.segment[seg-1].ycor()
            self.segment[seg].goto(new_x,new_y)
        
        self.head.forward(MOVE_BY_STEPS)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.segment[0].setheading(90)
    def down(self):
        if self.head.heading() != UP:
            self.segment[0].setheading(270)
    def right(self):
        if self.head.heading() != LEFT:
            self.segment[0].setheading(0)
    def left(self):
        if self.head.heading() != RIGHT:
            self.segment[0].setheading(180)