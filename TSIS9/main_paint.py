import pygame

pygame.init()

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paint in Python')

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60
clock = pygame.time.Clock()

start_to_draw = False
sp = ep = None

screen_close = False

while not screen_close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            start_to_draw = True
            sp = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if start_to_draw:
                pos = event.pos

                width = pos[0] - sp[0]
                height = pos[1] - sp[1]

                screen.fill(WHITE)
                pygame.draw.rect(screen, RED, (sp[0], sp[1], width, height))
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            start_to_draw = False
            