from turtle import Turtle
import random

COLORS = ["red", "blue", "green"]


class Molecule(Turtle):

    def __init__(self, board_w, board_h, speed):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.size = 0.5
        self.shapesize(self.size, self.size)
        self.penup()
        self.board_w = board_w
        self.board_h = board_h
        self.speed = speed
        x = random.randint(-0.95*board_w/2, 0.95*board_w/2)
        y = random.randint(-0.95*board_h/2, 0.95*board_h/2)
        self.goto(x, y)
        self.direction = random.randint(0, 360)
        self.setheading(self.direction)

    def move(self, m_mode):
        if m_mode == 0:
            self.direction = random.randint(0, 360)
            self.setheading(self.direction)
        self.forward(self.speed)

    def bounce(self, b_mode, m_mode):
         if b_mode == 0:     # no borders
            pass
         elif b_mode == 1:     # normal borders
            if m_mode == 0: # chaotic move
                if self.xcor() < -self.board_w/2:
                    self.goto(-self.board_w/2, self.ycor())
                elif self.xcor() > self.board_w/2:
                    self.goto(self.board_w/2, self.ycor())
                elif self.ycor() < -self.board_h/2:
                    self.goto(self.xcor(), -self.board_h/2)
                elif self.ycor() > self.board_h/2:
                    self.goto(self.xcor(), self.board_h/2)
                self.speed = -self.speed
            if m_mode == 1:               # normal move
                angle = self.heading()

                if self.ycor() > self.board_h/2 or self.ycor() < -self.board_h/2:
                    if 0 < angle < 180:
                        self.setheading(0 - angle)
                    else:
                        self.setheading(360 - angle)

                elif self.xcor() > self.board_w/2 or self.xcor() < -self.board_w/2:

                    if 0 < angle < 180:
                        self.setheading(180 - angle)
                    else:
                        self.setheading(540 - angle)

         elif b_mode == 2:       # virtual borders
            x = random.randint(-0.95 * self.board_w / 2, 0.95 * self.board_w / 2)
            y = random.randint(-0.95 * self.board_h / 2, 0.95 * self.board_h / 2)
            self.goto(x, y)

    def size_increase(self, r1, r2):

        rx = (r1 ** 3 + r2 ** 3) ** 0.333   # from the formula for the volume of a sphere
        self.size = rx
        self.shapesize(self.size, self.size)
        new_color = random.choice(COLORS)
        self.color(new_color)
