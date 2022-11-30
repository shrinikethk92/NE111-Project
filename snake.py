"""Snake, classic arcade game.
Comments by: Shriniketh Kothandaraman, 21016397
"""

from random import randrange  # randrange method returns random element between given parameters
from turtle import *  # imports everything from turtle package - Graphics

from freegames import square, vector  # imports vector coordinate system, imports square object

food = vector(0, 0)  # starting position of the food (origin)
snake = [vector(10, 0)]  # starting vector of the snake
aim = vector(0, -10)  # vector direction snake will move in


def change(x, y):  # function to change snake direction

    aim.x = x  # x direction of snake
    aim.y = y  # y direction of snake


def inside(head):  # Function to determine if snake is within bounds

    return -200 < head.x < 190 and -200 < head.y < 190  # returns true if the snake is in boundaries


def move():  # Function to move and expand snake

    head = snake[-1].copy()  # copies the parameters for the snake head, then adds it to the snake extending size
    head.move(aim)  # moves the head in the direction of the aim vector

    if not inside(head) or head in snake:  # if snake is not in bounds, or if head collides with the snake:
        square(head.x, head.y, 9, 'red')  # stops snake from moving, and changes colour of the head of snake to red
        update()  # updates the list containing the snake to make it stop moving
        return  # returns nothing

    snake.append(head)  # appends the new value (additional square) to head, essentially adding it to the snake.

    if head == food:  # If head of snake makes contact with food
        print('Snake:', len(snake))  # prints snake + the length of the snake
        food.x = randrange(-15, 15) * 10  # randomly generates new x-coordinate for next food )between (-150 and 150 x)
        food.y = randrange(-15, 15) * 10  # randomly generates new x-coordinate for next food )between (-150 and 150 y)
    else:
        snake.pop(0)  # removes first indexed value to remove the square in the previous position

    clear()  # clears all existing entries in the list

    for body in snake:
        square(body.x, body.y, 9, 'black')  # controls coordinate of body, size of body, and colour

    square(food.x, food.y, 9, 'green')  # controls vector coordinates of the food, the size of the food, and the colour
    update()  # updates specified value into the dictionary
    ontimer(move, 100)  # automatically moves snake after 100 ms


setup(420, 420, 370, 0)  # dimensions of the screen
hideturtle()  # hides the turtle
tracer(False)  # turns automatic screen updates off
listen()  # allows user to interact with turtle by listening to keystrokes
onkey(lambda: change(10, 0), 'Right')  # calls change function and sets x value = 10, y value = 0 (right)
onkey(lambda: change(-10, 0), 'Left')  # calls change function and sets x value = -10, y value = 0 (left)
onkey(lambda: change(0, 10), 'Up')  # calls change function and sets x value = 0, y value = 10 (up)
onkey(lambda: change(0, -10), 'Down')  # calls change function and sets x value = 0, y value = -10 (down)
move()  # calls move function
done()  # calls done function
