from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.7)
        self.color("blue")
        self.speed("slowest")
        self.penup()

    def placement(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))