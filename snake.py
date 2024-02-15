from turtle import Turtle


class Snake:
    def __init__(self):
        self.list = []

    def creation(self):
        for part in range(3):  # Initiating a snake that consists of 3 dots as a start.
            self.add_dot((part*-20, 0))
        self.head = self.list[0]

    def add_dot(self, position):
        dot = Turtle("square")
        dot.color("white")
        dot.speed("slowest")
        dot.penup()
        dot.goto(position)
        self.list.append(dot)

    def extend(self):
        self.add_dot(position=self.list[-1].position())

    def move(self):
        for n in range(len(self.list)-1, 0, -1):
            self.list[n].goto(self.list[n-1].position())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def reset(self):
        for dot in self.list:
            dot.hideturtle()
        self.list = []
        self.creation()
        self.head.goto(0, 0)