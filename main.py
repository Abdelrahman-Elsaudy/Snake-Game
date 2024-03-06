# How I Wrote This Code:
# Step_1: Creating the screen and the snake
# Step_2: Creating snake motion logic, which is each segment of it moves to the position of the former segment
#         then the snake head moves forward, then repeat.
# Step_3: Assigning the redirection of the snake to up, down, left and right buttons
#         and making sure that it can't turn in the opposite direction with one click, so it doesn't hit itself.
# Step_4: Defining the screen borders and snake collision with them
# Step_5: Creating the extension logic of the snake which is placing the new segment at the end of it then it
# #         follows the motion logic.
# Step_6: Creating snake food and extending the snake when it hits it.
# Step_7: Detecting when the snake hits itself.
# Step_8: Keeping track of score, saving the highest score in a file to recall it, and saving the top scorer name.
# Step_9: When the player loses, asking them if they want to keep playing.
# Step_9: Resetting snake and score when the player decides to keep playing.

import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
snake.creation()

food = Food()
food.placement()

score = Score()
score.update_scoreboard()


def screen_interaction():
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


game_on = True
while game_on:

    # While snake is between borders.
    while -300 < snake.head.xcor() < 300 and -300 < snake.head.ycor() < 300:
        screen.update()
        screen_interaction()
        time.sleep(0.1)
        snake.move()

        # When snake hits food.
        if snake.head.distance(food) < 20:
            food.placement()
            snake.extend()
            score.increase_score()

        # When snake hits itself.
        snake_hits_itself = False
        for dot in snake.list:
            if dot != snake.head and snake.head.distance(dot) < 10:
                snake_hits_itself = True
        if snake_hits_itself:
            break

    # Continue playing?
    keep_playing = screen.textinput("GAME OVER!", "Type y to continue playing.")
    if keep_playing == "y":
        score.reset()
        snake.reset()
    else:
        game_on = False

screen.exitonclick()
