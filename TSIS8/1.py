# just for test
import pygame
from pygame.locals import *

pygame.init()

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
# Side note: If you didn’t import everything from pygame.locals as we did you would have to 
# use pygame.locals.QUIT instead of QUIT.
screen = pygame.display.set_mode((300, 300))


