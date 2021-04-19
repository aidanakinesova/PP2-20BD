from snake_class import Snake
import pygame 
import time
import random
import pickle

pygame.init()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 102)
GREEN = (0, 255, 0)

WIDTH = 800
HEIGHT = 600

wall_points = []
# image = pygame.image.load('firewall.png')

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake game")

snake_block_size = 10
snake_speed = 10

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("papyrusttc", 20)
score_font = pygame.font.SysFont("ヒラキノ角コシックw0ttc", 35)
level_font = pygame.font.SysFont('papyrusttc', 65)
number_font = pygame.font.SysFont('papyrusttc', 150)

FILE_NAME = 'snakes_saved.data'

# def level():
#     file = open('level2.txt', 'r').readlines()
#     for i in range(len(file)):
#         for j in range(len(file[i])):
#             if file[i][j] == '#':
#                 screen.blit('firewall.png', (j * snake_block_size, i * snake_block_size))
#                 wall_points.append((j * snake_block_size, i * snake_block_size))

def message(font, msg, color, x, y):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, (x, y))

def game_loop():
    global snake_speed
    game_over = False
    game_close = False
    choose = False
    level_counter = 0
    level_choice = False
    snake1 = Snake(snake_block_size, snake_speed , BLACK, [WIDTH // 2, HEIGHT // 2])
    keys = {
        'UP': pygame.K_UP,
        'DOWN': pygame.K_DOWN,
        'RIGHT': pygame.K_RIGHT,
        'LEFT': pygame.K_LEFT
    }
    snake2 = Snake(snake_block_size, snake_speed , WHITE, [WIDTH // 2 + 50, HEIGHT // 2], keys = keys)
    snakes = (snake1, snake2)
    while not choose:
        screen.fill(BLUE)
        message(font_style, "Press space to load saved game, or other button to start a new one", GREEN, WIDTH // 5, HEIGHT // 2)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    try:
                        with open(FILE_NAME, 'br') as f:
                            snakes = pickle.load(f)
                            choose = True   
                    except Exception as e:
                        print(e)
                        snakes = (snake1, snake2)
                        choose = True
                else:
                    while not level_choice:
                        screen.fill(YELLOW)
                        pygame.display.update()
                        message(score_font, "Choose level: ", BLACK, WIDTH // 4, HEIGHT // 4)
                        pygame.display.update()
                        message(level_font, "1 ", BLACK, WIDTH // 4, HEIGHT // 3)
                        pygame.display.update()
                        message(level_font, "2", BLACK, WIDTH // 3, HEIGHT // 3)
                        pygame.display.update()
                        message(level_font, "3", BLACK, WIDTH // 2.5, HEIGHT // 3)
                        pygame.display.update()
                        time.sleep(1)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_1:
                                    level_counter = 0
                                    choose = True
                                    level_choice = True   
                                if event.key == pygame.K_2:
                                    level_counter = 1
                                    choose = True
                                    level_choice = True 
                                if event.key == pygame.K_3:
                                    snake_speed = 20
                                    level_counter = 2
                                    choose = True
                                    level_choice = True 
                    # snakes = (snake1, snake2)
    
    foodx = round(random.randrange(0, WIDTH - snake_block_size) / float(snake_block_size)) * float(snake_block_size)
    foody = round(random.randrange(0, HEIGHT - snake_block_size) / float(snake_block_size)) * float(snake_block_size)
    
    while not game_close:
        clock.tick(snake_speed)

        while game_over:
            screen.fill(BLUE)
            message(level_font, "Game over!", RED, WIDTH // 3, HEIGHT // 2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_close = True
                    if event.key == pygame.K_c:
                        game_loop()
        screen.fill(BLUE)
        for snake in snakes:
            snake.draw(screen)
        wall_image = pygame.image.load('firewall.png')
        levels = ['level1.txt', 'level2.txt', 'level3.txt']
        file = open(levels[level_counter], 'r').readlines()
        for i in range(len(file)):
            for j in range(len(file[i])):
                if file[i][j] == '#':
                    wall_points.append((j * snake_block_size, i * snake_block_size))
                    screen.blit(wall_image, (j * snake_block_size, i * snake_block_size))
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    with open(FILE_NAME, 'bw') as f:
                        pickle.dump(snakes, f)
                    game_close = True

        for snake in snakes:
            x1, y1 = snake.get_head_coordinates()
            if x1 > WIDTH or x1 < 0 or y1 > HEIGHT or y1 < 0:
                game_over = True
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, WIDTH - snake_block_size) / float(snake_block_size)) * float(snake_block_size)
                foody = round(random.randrange(0, HEIGHT - snake_block_size) / float(snake_block_size)) * float(snake_block_size)
                snake.add_block()
        for point in wall_points:
            x0, y0 = snakes[0].get_head_coordinates()
            x1, y1 = snakes[1].get_head_coordinates()
            if (x0 == point[0]  and y0 == point[1]) or (x1 == point[0] and y1 == point[1]):
                game_over = True
            if foodx == point[0] and foody == point[1]:
                foodx = round(random.randrange(0, WIDTH - snake_block_size) / float(snake_block_size)) * float(snake_block_size)
                foody = round(random.randrange(0, HEIGHT - snake_block_size) / float(snake_block_size)) * float(snake_block_size)

        pressed_keys = pygame.key.get_pressed()

        for snake in snakes:
            snake.move(pressed_keys)

        
        pygame.draw.rect(screen, GREEN, [foodx, foody, snake_block_size, snake_block_size]) 
        

        message(score_font, "Black score: " + str(snakes[0].get_length() - 1), YELLOW, 0, 0)
        message(score_font, "White score: " + str(snakes[1].get_length() - 1), YELLOW, WIDTH - 200, 0)
   
        pygame.display.update()
            
    pygame.quit()
    quit()

if __name__ == '__main__':
    game_loop()