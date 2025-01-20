from turtle import Screen,Turtle
from ball import Ball
from paddle import Paddle
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Atish's Pong")
screen.tracer(0)

paddle1 = Paddle(350, 0)
paddle1.color("red")
paddle2 = Paddle(-350, 0)
paddle2.color("blue")

ball = Ball()

score = Score()

# For drawing the line at the midway of the game of the screen
line = Turtle()
line.color("white")
line.penup()
line.goto(0, 300)
line.setheading(270)
while line.ycor() != -300:
    line.pendown()
    line.forward(10)
    line.hideturtle()

screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)  # speed of the ball is changed through here
    screen.update()
    ball.move_ball()
    # bouncing the ball of the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball()

    # detecting the collision with the paddle
    if (ball.xcor() == 330 and ball.distance(paddle1) < 50) or (ball.xcor() == -330 and ball.distance(paddle2) < 50):
        ball.bounce_paddle()

    # reset the ball after going out from the right side
    if ball.xcor() > 380:
        score.increase_l_score()
        ball.reset_game()
        paddle1.goto(350, 0)
        paddle2.goto(-350, 0)

    # reset the ball after going out from the left side
    if ball.xcor() < -380:
        score.increase_r_score()
        ball.reset_game()
        paddle1.goto(350, 0)
        paddle2.goto(-350, 0)

    # checking whether the winner is left one
    if score.l_score == 5:
        score.goto(0, 0)
        score.write("Blue one is the winner !!", align="center", font=("Arial", 30, "normal"))
        game_on = False

    # checking whether the winner is right one
    if score.r_score == 5:
        score.goto(0, 0)
        score.write("Red one is the winner !!", align="center", font=("Arial", 30, "normal"))
        game_on = False

screen.exitonclick()
