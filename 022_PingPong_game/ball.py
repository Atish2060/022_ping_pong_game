from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("purple")
        self.shapesize(1, 1)
        self.new_xcor = 10
        self.new_ycor = 10
        self.move_speed = 0.1  # for changing the speed of the ball everytime it hits the paddle

    def move_ball(self):
        new_x_cor = self.xcor()
        new_y_cor = self.ycor()
        self.penup()
        self.goto(new_x_cor + self.new_xcor, new_y_cor + self.new_ycor)

    def bounce_ball(self):
        self.new_ycor = self.new_ycor * -1

    def bounce_paddle(self):
        # self.new_ycor = self.new_ycor * -1
        self.new_xcor = self.new_xcor * -1
        self.move_speed *= 0.9  # here the speed of the ball is changed

    def reset_game(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_paddle()  # it pushes the ball in the positive x or negative x direction








