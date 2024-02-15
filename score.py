from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("high_score.txt") as file:
                self.high = int(file.read())
        except FileNotFoundError:
            self.high = None
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high}", align=ALIGNMENT, font=FONT)

    def save_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high}")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.high is None or self.score > self.high:
            self.high = self.score
            self.save_score()
        self.score = 0
        self.update_scoreboard()