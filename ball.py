from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        #self.speed(0.1)
        self.x_move = 10
        self.y_move = 10
        self.move()

    def move(self):
        self.newy = self.ycor() + self.y_move
        self.newx = self.xcor() + self.x_move
        self.goto(x=self.newx, y=self.newy)


    def bounce(self):
        self.y_move *= -1


    def resetball(self):
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10


    def hit(self):
        self.x_move *= -1

    def speedup(self):
        self.x_move *= 1.2
        self.y_move *= 1.2