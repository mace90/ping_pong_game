from turtle import Turtle

class Score(Turtle):
    def __init__(self, xpos, ypos):
        super(Score, self).__init__()
        self.goto(x=xpos, y=ypos)
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.write(arg=f"{self.score}", font=("Courier", 50, "normal"))
        self.penup()


    def addpoint(self):
        self.clear()
        self.score += 1
        self.write(arg=f"{self.score}", font=("Courier", 50, "normal"))