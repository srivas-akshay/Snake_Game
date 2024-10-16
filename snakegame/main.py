# Importing required modules

from turtle import Turtle,Screen,write
import time
from snake import Snake
from food import Food
from scoreboard import Score_Board

scoreboard = Score_Board()
screen = Screen()
screen.title("                                                                      My Snake Game ")
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
snake = Snake()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

food = Food()

# Main Execution  of Sanke Game 

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.Move()

    if snake.head.distance(food) < 15 :
        food.Goto()
        snake.extend()
        scoreboard.Update_Score()   
    # ditect collision  
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 ) or (snake.head.ycor() > 280 or snake.head.ycor() < -280 ):
        game_is_on = False
        scoreboard.collision()
    # ditect collision wih snake tail.
    for seg in snake.segment:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.collision()
screen.exitonclick()