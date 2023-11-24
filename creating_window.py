# import pygame module
import pygame
from sys import exit

# call the pygame.init()
pygame.init()

# set the display
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

# change window name
pygame.display.set_caption('Chase')

# create a while loop to update display and also enable quit event which allow player to quit display
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # draw all elements and update everything
    pygame.display.update()
    clock.tick(60)