"""Cannon, classic arcade game.
Comments by: Khanij Bhatdwaj; 21009633
Shriniketh Kothandaraman; 21016397
"""



from random import randrange    #   Returns random elements from between defined range
from turtle import *    #   Imports Objects from turtle
from freegames import vector    #   Imports vector coordinate system and square object

ball = vector(100, 100) #   Starting Position of the Balls
speed = vector(0, 0)    #   Starting Speed of the balls
targets = []

def inside(xy): #Function to determine whether the balls are within the given border

    return -600 < xy.x < 600 and -900 < xy.y < 900


def draw():     #A function to Draw the balls
    clear() #   clears all existing entries in the list

    for target in targets:
        goto(target.x, target.y)    #   Sets position of the balls spawn point
        dot(30, 'red')  #   Changes the Size in diameter and color of the balls
        dot(15, 'blue')


def move(): # A function to move the balls

    if randrange(10) == 0:
        y = randrange(-400, 400)
        target = vector(100, y)
        targets.append(target)

    for target in targets:     #    Changes the speed of the balls
        target.x -= 10

    #    if inside(ball):
    #        speed.y -= 10
    #        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 10:
            targets.append(target)

    draw()

    #   for target in targets:
    #      if not inside(target):
    #          return

    ontimer(move, 20)


setup(600, 600, 400, 0) #   Sets Up the game dimensions(window)
hideturtle()    #   Hides the Turtle
up()    #   Calls up function
tracer(False)   #Turns automatic screen updates off
move()  #   calls move function
done()  #calls done function