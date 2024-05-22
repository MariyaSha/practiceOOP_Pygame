import pygame
import random
import os

# place Pygame window at a specific location
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)
    
# pygame settings
pygame.init()
screen = pygame.display.set_mode((800, 800))
running = True

# load image and set its location
img = pygame.image.load("sedan_red.png")
img_location = img.get_rect()
img_location.center = 400, 400

# set background colour
screen.fill("white")
# place image on the screen
screen.blit(img, img_location)

# start game loop
while running:
    # if we click on the "exit" button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # stop game loop
            running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()

