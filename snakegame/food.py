from turtle import Turtle
import random
"""This is a food.py in this file we are achieve the food of a snake in random postion every time when it colide."""
class Food(Turtle):
    """This is a foodclass in which it create a food object in main.py"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("white")
        self.penup()
        self.Goto()
    def Goto(self):
        # This function refresh the position of a food of a snake in random position between 600 by 600 area of square.
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)