# Paint
import pygame, random, time

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# (x1, y1), (x2, y2)
# A = y2 - y1
# B = x1 - x2
# C = x2 * y1 - x1 * y2
# Ax + By + C = 0
# (x - x1) / (x2 - x1) = (y - y1) / (y2 - y1)

def drawLine(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)



def main():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Paint')
    screen.fill(BLACK)
    pygame.display.update()
    mode = 'random'
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 10

    run = False

    def draw_rect():                         
        draw_on = True
        while run:
            rectx, recty = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        draw_on = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pygame.draw.rect(screen, (0, 0, 0), (rectx, recty, random.randrange(5, 200), random.randrange(5, 200)), 2)
            pygame.display.update()  

    def draw_circle():      
        draw_on = True
        while run:
            cirx, ciry = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    draw_on = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        draw_on = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pygame.draw.circle(screen, (0, 0, 0), (cirx, ciry), random.randrange(5, 100), 2)
            pygame.display.update()      

    colors = {
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0)
    }
    
    game_exit = False

    while not game_exit:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                if event.key == pygame.K_b:
                    mode = 'blue'
                if event.key == pygame.K_g:
                    mode = 'green'
                if event.key == pygame.K_q:
                    draw_rect()
                if event.key == pygame.K_w:
                    draw_circle()
                if event.key == pygame.K_UP:
                    radius += 1
                if event.key == pygame.K_DOWN:
                    radius -= 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 'random':
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                else:
                    color = colors[mode]
                pygame.draw.circle(screen, color, event.pos, radius)
                draw_on = True
            if event.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if event.type == pygame.MOUSEMOTION:
                if draw_on:
                    drawLine(screen, last_pos, event.pos, radius, color)
                    # pygame.draw.circle(screen, color, event.pos, radius)
                last_pos = event.pos
        pygame.display.flip()

    pygame.quit()

main()

# import pygame, random

# # (x1, y1) (x2, y2)
# # A = y2 - y1
# # B = x1 - x2
# # C = x2 * y1 - x1 * y2 

# def draw_line(screen, start, end, width, color):
#     x1 = start[0]
#     y1 = start[1]
#     x2 = end[0]
#     y2 = end[1]

#     dx = abs(x1 - x2)
#     dy = abs(y1 - y2)

#     if dx > dy:
#         if x1 > x2:
#             x1, x2 = x2, x1
#             y1, y2 = y2, y1
#         A = y2 - y1
#         B = x1 - x2
#         C = x2 * y1 - x1 * y2

#         for x in range(x1, x2):
#             y = (-C - A * x) / B
#             pygame.draw.circle(screen, color, (x, y), width)
#     else:
#         if y1 > y2:
#             x1, x2 = x2, x1
#             y1, y2 = y2, y1 
#         for y in range(y1, y2):
#             x = (-C - B * y) / A
#             pygame.draw.circle(screen, color, (x, y), width)

# def main():
#     WHITE = (255, 255, 255)
#     screen = pygame.display.set_mode((800, 600))
#     screen.fill(WHITE)
#     pygame.display.update()
#     mode = 'random'
#     draw_on = False
#     last_pos = (0, 0)
#     color = (255, 128, 0)
#     radius = 10

#     colors = {
#         'red': (255, 0, 0),
#         'blue': (0, 0, 255),
#         'green': (0, 255, 0)
#     }

#     while True:
#         pressed = pygame.key.get_pressed()
#         alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
#         ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 return
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_w and ctrl_held:
#                     return
#                 if event.key == pygame.K_F4 and alt_held:
#                     return
#                 if event.key == pygame.K_r:
#                     mode = 'red'
#                 if event.key == pygame.K_b:
#                     mode = 'blue'
#                 if event.key == pygame.K_g:
#                     mode = 'green'
#                 if event.key == pygame.K_c:
#                     pygame.draw.rect(screen, )
#                 if event.key == pygame.K_UP:
#                     radius += 1
#                 if event.key == pygame.K_DOWN:
#                     radius -= 1
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if mode == 'random':
#                     color = (random.randrange(256), random.randrange(256), random.randrange(256))
#                 else:
#                     color = colors[mode]
#                 pygame.draw.circle(screen, color, event.pos, radius)
#                 draw_on = True
#             if event.type == pygame.MOUSEBUTTONUP:
#                 draw_on = False
#             if event.type == pygame.MOUSEMOTION:
#                 if draw_on:
#                     draw_line(screen, last_pos, event.pos, radius, color)
#                     # pygame.draw.circle(screen, color, event.pos, radius)
#                 last_pos = event.pos
#         pygame.display.flip()

#     pygame.quit()

# main()