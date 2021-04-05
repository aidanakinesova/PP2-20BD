from os import supports_bytes_environ
import pygame
import sys
import math

WIDTH = 700
HEIGHT = 450
pygame.init()
screen = pygame.display.set_mode([WIDTH  , HEIGHT])
font = pygame.font.SysFont('calibri', 20)
main_x = font.render('X',False,[0,0,0])
sin_t = font.render('sin',False,[0,0,0])
cos_t = font.render('cos',False,[0,0,0])

font2 = pygame.font.SysFont('calibri', 15)
y_values = ["1.00","0.75","0.50","0.25","0.00","-0,25","-0.50","-0.75","-1.00"]
x_values = ["-3П","-2.5П","-2П","-1.5П","-П","-0.5П","0","0.5П","П","1.5П","2П","2.5П","3П"]

screen.fill((255, 255, 255))
A = 150
mp = 50

class Point:
    # constructed using a normal tupple
    def __init__(self, point_t=(0, 0)):
        self.x = float(point_t[0])
        self.y = float(point_t[1])
    # define all useful operators
    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))
    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))
    def __mul__(self, scalar):
        return Point((self.x*scalar, self.y*scalar))
    def __div__(self, scalar):
        return Point((self.x/scalar, self.y/scalar))
    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))
    # get back values in original tuple format
    def get(self):
        return (self.x, self.y)

def draw_dashed_line(surf, color, start_pos, end_pos, width = 1, dash_length = 4):
    origin = Point(start_pos)
    target = Point(end_pos)
    displacement = target - origin
    length = len(displacement)
    slope = displacement.__div__(length)
    for index in range(0, int(length/dash_length), 2):
        start = origin + (slope * index * dash_length)
        end = origin + (slope * (index + 1) * dash_length)
        pygame.draw.aaline(surf, color, start.get(), end.get(), width)

def get_points(function, xrange, step, kx, ky, move):
    all_numbers = math.ceil((xrange[1] - xrange[0]) / step) 
    all_x = (x * step + xrange[0] for x in range(all_numbers))  
    pre_points = ((kx * x, ky * function(x)) for x in all_x)
    points = tuple(map(lambda x: (x[0] + move[0], -x[1] + move[1]), pre_points))
    return points

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE:
                sys.exit()
        cos_points = []
        sin_points =  []
        xrange_in_pixels = WIDTH - 100
        kx =  xrange_in_pixels / (6 * math.pi)
        ky =  2 * A  / 2
        sin_points = get_points(math.sin, (-3 * math.pi, 3 * math.pi) , 0.2 , kx,ky ,(WIDTH/2,HEIGHT/2 - mp / 2))
        cos_points = get_points(math.cos, (-3 * math.pi, 3 * math.pi) , 0.2 , kx,ky ,(WIDTH/2,HEIGHT/2 - mp / 2))
        '''
        top_left_for_rect = (mp,mp)
        top_right_for_rect = (xrange,mp)
        down_left_for_rect = (mp, 2 * A)
        down_right_for_rect = (xrange,2 * A)
        pygame.draw.rect(screen,[0,0,0],[top_left_for_rect, down_right_for_rect ],1) # inside rect
        '''
        
        top_x,top_y = mp - 20 , mp - 20
        down_x,down_y = xrange_in_pixels + 40, 2 * A + 40
        pygame.draw.line(screen,[0,0,0],(mp,top_y),(mp,2 * A + 69))
        pygame.draw.line(screen,[0,0,0],(top_x,mp),(down_x + 29,mp))
        pygame.draw.line(screen,[0,0,0],(top_x,down_y + 11),(down_x + 29, down_y + 11))
        pygame.draw.line(screen,[0,0,0],(down_x + 11,top_y),(down_x + 11,2 * A + 50 + 19))
        
        pygame.draw.rect(screen,[0,0,0],[(top_x,top_y), (down_x,down_y) ],1) #outside rect
        c = xrange_in_pixels / 6 / 8
        k = math.ceil(2 * A  / 8) / 4 
        #Hor lines down
        for i in range(0,48):
                pygame.draw.line(screen,[0,0,0],(mp + i * c,down_y + 25 ),(mp + i * c,down_y + 29))
        for i in range(0,48,2):
                pygame.draw.line(screen,[0,0,0],(mp + i * c,down_y + 20 ),(mp + i * c,down_y + 29))
        for i in range(0,48,4):
                pygame.draw.line(screen,[0,0,0],(mp + i * c,down_y + 16 ),(mp + i * c,down_y + 29))
        #Hor lines up
        for i in range(0,48):
                pygame.draw.line(screen,[0,0,0],(mp + i * c,top_y  ),(mp + i * c,top_y + 4))
        for i in range(0,48,2):
                pygame.draw.line(screen,[0,0,0],(mp + i * c,top_y  ),(mp + i * c,top_y + 9))
        for i in range(0,48,4):
                pygame.draw.line(screen,[0,0,0],(mp + i * c,top_y  ),(mp + i * c,top_y + 13))
        #Ver lines left
        for i in range(0,32):
                pygame.draw.line(screen,[0,0,0],(top_x , mp + i * k),(top_x + 4,mp + i * k))
        for i in range(0,32,2):
                pygame.draw.line(screen,[0,0,0],(top_x ,mp  + i * k),(top_x + 9,mp + i * k))
        for i in range(0,32,4):
                pygame.draw.line(screen,[0,0,0],(top_x ,mp  + i * k),(top_x + 29,mp + i * k))
        #Ver lines right     
        for i in range(0,32):
                pygame.draw.line(screen,[0,0,0],(down_x + 25, mp + i * k),(down_x + 29,mp + i * k))
        for i in range(0,32,2):
                pygame.draw.line(screen,[0,0,0],(down_x + 20,mp  + i * k),(down_x + 29,mp + i * k))
        for i in range(0,32,4):
                pygame.draw.line(screen,[0,0,0],(down_x + 29,mp  + i * k),(down_x, mp + i * k))
        #Text of X and Y values
        j = 0
        for i in range(len(x_values)):
                x_val = font2.render(x_values[i],False,[0,0,0])
                screen.blit(x_val,(mp +  j - 5,down_y + 35))
                j+= (c * 4)
        j = 0
        for i in range(len(y_values)):
                y_val = font2.render(y_values[i],False,[0,0,0])
                screen.blit(y_val,(1,mp + j - 8))
                j+= (k * 4)
        ###
        point_for_text = 0
        for i in range(0,xrange_in_pixels,math.ceil(xrange_in_pixels/6)):
                if i == int(xrange_in_pixels/6) * 4:
                        pygame.draw.line(screen, [0,0,0] , (50 + i,50 + A / 4),(50 + i,50 + 2 * A))
                        point_for_text = i
                else:pygame.draw.line(screen, [0,0,0] , (50 + i,50 - 20),(50 + i,50 + 2 * A + 11))
        for i in range(0, 2 * A, math.ceil((2 * A )/ 8)):
                pygame.draw.line(screen, [0,0,0] , (50 , 50+ i),(50 + xrange_in_pixels,50 + i))

        draw_dashed_line(screen,[0,0,255],(point_for_text+ mp + 20,mp + 30),(point_for_text+ mp * 2,mp + 30),1,4)
        pygame.draw.line(screen,[255,0,0],(point_for_text+ mp + 20,mp + 10),(point_for_text+ mp * 2,mp + 10))
        
        screen.blit(main_x,(mp + (xrange_in_pixels/2), 2 * A + mp * 2))
        screen.blit(sin_t,(point_for_text+ 40,mp))
        screen.blit(cos_t,(point_for_text+ 40,mp + 20))
        
        for i in range(len(cos_points) - 1):
                draw_dashed_line(screen,[0,0,255],cos_points[i],cos_points[i+1],1,4)
        
        pygame.draw.aalines(screen, [255, 0,0], False, sin_points)
        #pygame.draw.aalines(screen, [0, 0, 255], False, cos_points)

        pygame.display.flip()