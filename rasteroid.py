'''
Comments by: Shriniketh Kothandaraman (21016397)
             Khanij Bhardwaj(21009633)

'''

import pygame # imports pygame module - K
import time # imports time module - K 
import random # imports module - K 

pygame.init()  # initializes pygame module - K

score = 0  # sets initial score to be 0 - S
counter = 0  # spawns asteroid when counter hits 15 (1 every 1/2 second) - K
black = (0, 0, 0) # defines black as the RGB value0 (0, 0, 0) - K
white = (255, 255, 255) #defines white as the RGB value (255, 255, 255) - K

width = 800  # screen dimension - K
height = 800  # screen dimension - K
display = pygame.display.set_mode((width, height))  # displays dimensions - K
pygame.display.set_caption('Rasteroid')  # name of the game - K
clock = pygame.time.Clock()  # starts clock (fps) - K

playerx = 15  # startpos - S 
playery = height / 2  # startpos - S
movement = 0  # not moving initially - S
charspeed = 50  # speed of the character - S
gameover = False  # default setting: game is running - S
array = []  # empty array (will contain all spawned asteroids) - S

asteroidImg = pygame.image.load(
    "./asteroid.png").convert()  # load asteroid img - S
shipImg = pygame.image.load("./spaceship.png").convert()  # load ship img - S
asteroidImg = pygame.transform.scale(
    asteroidImg, (40, 40))  # resize asteroid img
shipImg = pygame.transform.scale(shipImg, (30, 30))  # resize ship img - S

class cb:  # creates class of asteroid - S
    def __init__(self, height):  # initialize asteroid - S
        """
        Creates a function of asteroid which can be called later to create multiple instances.
        Args:
            height: 
        """
        self.cbx = 800  # starts at 800 x - K
        self.cby = random.randrange(0, height)  # random y value to start - K
        self.cballwidth = 40  # width of asteroid - K
        self.cballheight = 40  # height of asteroid - K
        self.color = white
        if score < 25:
            # random speed between 5 and 10 - S
            self.speed = random.randrange(1, 10)
        elif score >= 25 and score < 50:  # increase speed after 25 points - S
            # random speed between 11 and 20  - S
            self.speed = random.randrange(11, 20)
        elif score >= 50:  # increase speed after 50 points - S
            self.speed = random.randrange(21, 25)

    def cbmovement(self):  # movement of asteroid - S
        """ function for the speed of each instance of the asteroid spawned """
        # ballspeed = random.randrange(10,20) 
        self.cbx -= self.speed #sets cbx to subtract speed every frame - S

while not gameover: #while game is running - K
    counter += 1 #starts counter counting while loop is running - K
    display.fill(black) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if game is quit will change gameover to True, and quit - K
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # movement command - K
                movement = -5  # moves 5 pixels up - K
            elif event.key == pygame.K_DOWN:  # movement command - K
                movement = 5  # moves 5 pixels down - K

    if playery >= height or playery < 0:  # if player goes above or below screen, game will end - S
        gameover = True

    playery += movement  # adds movement command to the y position of player - K
    ship = shipImg.get_rect()  # creates a rectangle of the image - S
    # centers the rectangle to be aligned with the coordinates of the player - S
    ship.center = (playerx, playery)
    display.blit(shipImg, ship)  # blit maps the image onto the given location - S
    pygame.display.update(ship)  # updates display - S
    pygame.display.update()  # updates display - S

    # spawns asteroid every 30 frames (60 fps so spawns 1 every 0.5s) - K
    if counter % 30 == 0:
        asteroid = cb(height)
        array.append(asteroid) # appends each spawned asteroid into the empty array - S
    #    print('lol') -> testing - S

    if array:
        arrayToRemove = [] #empty array for now - S
        for i in range(len(array)):
            if array[i].cbx <= 0:  # if object goes out of bounds - S
                arrayToRemove.append(i) # appends(moves) the element of the array into the new empty array
                # score is added (may not work fully because asteroids may be too fast for array to update depending on PC performance - S
                score = score + 1 # adds one to the score (to increase speed) - S
            #    print (score) # -> testing - S

        for i in arrayToRemove: # for loop for new array - S
            array.pop(i) # deletes the element in the array - S
            '''
            This section of code looks a lot different from the video because we only noticed the bug with the array after recording the video, but creating a new array also gets rid of the issue where asteroids moved too fast for the array to update. It also fixed the issue of elements not getting removed as occasionally, an element that was not the first in the array would reach the other side faster then the first element of the array, so it would not delete. - S
            '''

    for i in range(len(array)):
        ast = array[i]  # assigns element i to ast - S
        ast.cbmovement()  # calls movement function to each element of the array - S
        recta = asteroidImg.get_rect()  # creates a rectangle of asteroid image - S
        recta.center = (ast.cbx, ast.cby) # centers rectangle of asteroid image - S
        display.blit(asteroidImg, recta)  # maps asteroid image onto rectangle - S
        pygame.display.update(recta)  # updates screen - S

        # recta = pygame.draw.rect(display, white, (ast.cbx, ast.cby, ast.cballwidth, ast.cballheight)) (ignore - S)
        # recta.blit(asteroidImg, (0,0)) (ignore - S)

        if playerx + 7.5 > ast.cbx - (ast.cballwidth/2) and playery + 7.5 > ast.cby - (ast.cballheight/2) and playery - 7.5 < ast.cby + (ast.cballheight/2):
           gameover = True  # collision detection for asteroids - K

    # print('new frame') -> testing - S
    # print (len(array))  #-> testing - S

    clock.tick(60)  # sets FPS to 60 - K

pygame.quit()  # quits game - K
quit()
