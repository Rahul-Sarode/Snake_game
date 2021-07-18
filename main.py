from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.2)
    snake.snake_movement()

    if snake.snake_head.distance(food) < 15:
        food.create_food()
        snake.extend()
        scoreboard.increase_score()

    if snake.snake_head.xcor() > 280 or snake.snake_head.ycor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for segment in snake.snake_objects[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
