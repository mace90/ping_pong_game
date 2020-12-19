from turtle import Turtle

LENOFPADDLE = 1.0
WIDOFPADDLE = 5.0


class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        # reminder for me: if i use the Turtle as the Superclass i dont have to write "paddle" before the attributes
        # for example self.shape("square") - without Superclass it would be: self.paddle = Turtle("square") or
        # self.paddle.penup() instead of self.penup()
        super().__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=WIDOFPADDLE, stretch_len=LENOFPADDLE)
#       self.speed("fastest")
        self.color("white")
        self.y = ycor
        self.x = xcor
        self.goto(self.x, self.y)


    def up(self):
        self.y += 20
        self.goto(self.x, self.y)

    def down(self):
        self.y += -20
        self.goto(self.x, self.y)



