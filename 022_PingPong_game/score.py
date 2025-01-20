from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 30, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 30, "normal"))

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_score()








