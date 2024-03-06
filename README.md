# The Snake Game

---

- The famous snake game in which a snake is chasing food and its length increases whenever it reaches the food, it dies if it hits the screen borders or it hits itself.
- This version saves the highest score achieved in a separate file, so it gets called every time the game is open
as the highest score achieved yet.

![snake_screenshot](https://github.com/Abdelrahman-Elsaudy/Snake-Game/assets/158151388/d26a7de2-6f08-494c-86a5-7f7db5829042)

---

## Applied Skills:

---

**1. Object-Oriented Programming**

Dividing the project into:
- `snake.py` which creates the snake, moves it in the 4 directions, extends it when it collides with food and resets it
when the game is over.
- `food.py` which creates the food dot and locates it randomly between the screen borders.
- `score.py` keeps track of the score, displays it along with the highest score achieved and resets the score when the game is over.
- `main.py` on which all of the above is called, the screen is set and the game_on loop works.


**2. Game Concept**

- The screen is updated inside a while loop on `main.py`, and each time it's updated each segment of the snake moves.
- Moving the snake in a way that makes all of its segments follow the head was challenging, starting with the last segment of the snake, each segment of it moves to the position of the segment before it 
  then the snake head moves forward or changes its direction, then repeat.
```
  def move(self):
    for n in range(len(self.list)-1, 0, -1):
        self.list[n].goto(self.list[n-1].position())
    self.head.forward(20)
```

- Defining the screen borders as the conditions in which the game is on, so if the snake passes any of them the game is over.
```
while game_on:
    # While snake is between borders.
    while -300 < snake.head.xcor() < 300 and -300 < snake.head.ycor() < 300:
        screen.update()
        screen_interaction()
        time.sleep(0.1)
        snake.move()
```
- Detecting when the snake hits the food which results in the food being placed in a random position, the snake extends and the score increases.
```
    if snake.head.distance(food) < 20:
        food.placement()
        snake.extend()
        score.increase_score()
```
- Snake extension: the extra part is placed at the end of the snake so the motion logic is applied to it and it follows the other segments.
```    
    def add_dot(self, position):
        dot = Turtle("square")
        dot.color("white")
        dot.speed("slowest")
        dot.penup()
        dot.goto(position)
        self.list.append(dot)

    def extend(self):
        self.add_dot(position=self.list[-1].position())
```
- Detecting when the snake hits itself.
```    
  snake_hits_itself = False
  for dot in snake.list:
      if dot != snake.head and snake.head.distance(dot) < 10:
          snake_hits_itself = True
  if snake_hits_itself:
      break
```
- If the snake hits any of the borders or hits itself, the game is over and the player is asked if they want to play again,
if they choose to play again, the snake and score are reset.
```    
    keep_playing = screen.textinput("GAME OVER!", "Type y to continue playing.")
    if keep_playing == "y":
        score.reset()
        snake.reset()
    else:
        game_on = False
```

---

## Bug Fixed:

- If the snake moves in a direction, and you press on the button that moves it in the opposite direction, you get "Game Over".
- This is because the head collides with the body.
- To fix it we have to prevent moving in the opposite direction with one click, so to move the snake down if it's moving up,
it has to move right or left first then move down to avoid colliding directly with its body.
```
    def up(self):
      if self.head.heading() != 270:
          self.head.seth(90)
```
- The same goes for defining down, left and right.
---

_Credits to: 100-Days of Code Course on Udemy._