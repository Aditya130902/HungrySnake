from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.turtles[0].distance(food) < 15:
        food.food_creation()
        snake.extend_snake()
        scoreboard.increase_score()

    if snake.turtles[0].xcor() > 280 or snake.turtles[0].xcor() < -299.99 or snake.turtles[0].ycor() > 300\
            or snake.turtles[0].ycor() < -280:
        scoreboard.reset_score_board()
        snake.reset()
    for snake_segment in snake.turtles[1:]:
        if snake.turtles[0].distance(snake_segment) < 10:
            scoreboard.reset_score_board()
            snake.reset()
screen.exitonclick()
