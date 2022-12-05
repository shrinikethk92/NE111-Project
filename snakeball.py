import pygame
import time
import random

pygame.init()  # initializes pygame module

score = 0  # sets initial score to be 0
counter = 0  # spawns asteroid when counter hits 15 (1 every 1/2 second)
black = (0, 0, 0)
white = (255, 255, 255)

width = 800  # screen dimension
height = 800  # screen dimension
display = pygame.display.set_mode((width, height))  # displays dimensions
pygame.display.set_caption('Spaceglider')  # name
clock = pygame.time.Clock()  # starts clock (fps)

playerx = 15  # startpos
playery = height / 2  # startpos
movement = 0  # not moving initially
charspeed = 50  # speed of the character
gameover = False  # default setting: game is running
array = []  # empty array (will contain all spawned asteroids)

asteroidImg = pygame.image.load(
    "./asteroid.png").convert()  # load asteroid img
shipImg = pygame.image.load("./spaceship.png").convert()  # load ship img
asteroidImg = pygame.transform.scale(
    asteroidImg, (40, 40))  # resize asteroid img
shipImg = pygame.transform.scale(shipImg, (30, 30))  # resize ship img


class cb:  # creates class of asteroid
    def __init__(self, height):  # initialize asteroid
        """_summary_

        Args:
            height (_type_): _description_
        """
        self.cbx = 800  # starts at 800 x
        self.cby = random.randrange(0, height)  # random y value to start
        self.cballwidth = 40  # width of asteroid
        self.cballheight = 40  # height of asteroid
        self.color = white
        if score < 25:
            # random speed between 5 and 10
            self.speed = random.randrange(1, 10)
        elif score >= 25 and score < 50:  # increase speed after 25 points
            # random speed between 11 and 20
            self.speed = random.randrange(11, 20)
        elif score >= 50:  # increase speed after 50 points
            self.speed = random.randrange(21, 25)

    def cbmovement(self):  # movement of asteroid
        """_summary_
        """
        # ballspeed = random.randrange(10,20)
        self.cbx -= self.speed


while not gameover:
    counter += 1
    display.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if game is quit will change gameover to True, and quit
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # movement command
                movement = -5  # moves 5 pixels up
            elif event.key == pygame.K_DOWN:  # movement command
                movement = 5  # moves 5 pixels down

    if playery >= height or playery < 0:  # if player goes above or below screen, game will end
        gameover = True

    playery += movement  # adds movement command to the y position of player
    ship = shipImg.get_rect()  # creates a rectangle of the image
    # centers the rectangle to be aligned with the coordinates of the player
    ship.center = (playerx, playery)
    display.blit(shipImg, ship)  # blit maps the image onto the given location
    pygame.display.update(ship)  # updates display
    pygame.display.update()  # updates display

    # spawns asteroid every 30 frames (60 fps so spawns 1 every 0.5s)
    if counter % 30 == 0:
        asteroid = cb(height)
        # appends each spawned asteroid into the empty array
        array.append(asteroid)
    #    print('lol') -> testing

    if array:
        if array[0].cbx < 0:  # if object goes out of bounds
            array.pop(0)  # removed from the array
            # score is added (may not work fully because asteroids may be too fast for array to update depending on PC performance)
            score = score + 1
        #    print (score) -> testing

    for i in range(len(array)):
        ast = array[i]  # assigns element i to ast
        ast.cbmovement()  # calls movement function to each element of the array
        recta = asteroidImg.get_rect()  # creates a rectangle of asteroid image
        # centers rectangle of asteroid image
        recta.center = (ast.cbx, ast.cby)
        display.blit(asteroidImg, recta)  # maps asteroid image onto rectangle
        pygame.display.update(recta)  # updates screen

        # recta = pygame.draw.rect(display, white, (ast.cbx, ast.cby, ast.cballwidth, ast.cballheight))
        # recta.blit(asteroidImg, (0,0))

    if playerx + 7.5 > ast.cbx - ast.cballwidth/2 and playery + 7.5 > ast.cby - ast.cballheight/2 and playery - 7.5 < ast.cby + ast.cballheight/2:
        gameover = True  # collision detection for asteroids

    # print('new frame') -> testing
    # print (len(array)) -> testing

    clock.tick(60)  # sets FPS to 60

pygame.quit()  # quits game
quit()
