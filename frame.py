from turtle import Turtle


class Frame(Turtle):

    def __init__(self, board_w, board_h, mode):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto((-board_w/2), (-board_w/2))
        self.setheading(90)
        self.pendown()
        if mode == 1:
            self.forward(board_h)
        elif mode == 2:
            for i in range(0, 50):
                self.forward(board_h/100)
                self.penup()
                self.forward(board_h/100)
                self.pendown()
        self.setheading(0)
        if mode == 1:
            self.forward(board_w)
        elif mode == 2:
            for i in range(0, 50):
                self.forward(board_w / 100)
                self.penup()
                self.forward(board_w / 100)
                self.pendown()
        self.setheading(270)
        if mode == 1:
            self.forward(board_h)
        elif mode == 2:
            for i in range(0, 50):
                self.forward(board_h / 100)
                self.penup()
                self.forward(board_h / 100)
                self.pendown()
        self.setheading(180)
        if mode == 1:
            self.forward(board_w)
        elif mode == 2:
            for i in range(0, 50):
                self.forward(board_w / 100)
                self.penup()
                self.forward(board_w / 100)
                self.pendown()
