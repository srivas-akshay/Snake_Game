from turtle import Turtle

ALINGMENT = "center"
FONT = ("San_sarif",15,"normal") 

class Score_Board(Turtle):
    """It represent the score board on the top by crating an object  """
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.print_score()

    def print_score(self):
        """for print the score"""
        self.write(f"Score : {self.score}" , font=FONT,align=ALINGMENT)
    
    def collision(self):
        """check if collision is held then it turns to Game over"""
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER !!!", font=FONT,align=ALINGMENT)
    def Update_Score(self):
        """update the score by one and print it"""
        self.score += 1
        self.clear()
        self.print_score()

        