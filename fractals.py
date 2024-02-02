import pygame
import math
pygame.init()

WINDOW = pygame.display.set_mode((1000,1000))

class Line():

    def __init__(self,r,alpha,WINDOW:pygame.Surface) -> None:

        self.r = r
        self.alpha = alpha
        self.x = r*math.cos(alpha)
        self.y = r*math.sin(alpha)
        self.WINDOW = WINDOW

    def getNextPos(self,start_pos):
        x,y = start_pos
        x+=int(self.x)
        y+=int(self.y)
        return((x,y))

    def draw(self,start_pos:list):
        next_pos = self.getNextPos(start_pos)
        pygame.draw.line(self.WINDOW,(0,0,0),start_pos,next_pos,1)
        return next_pos

def makeLine(current_lines:list[Line],generator_line:list[list[int]],WINDOW:pygame.Surface): # generator_line stored in form r , alpha
    
    new_line_list = []
    for old_line in current_lines:
        for new_line in generator_line:
            new_line_list.append(Line(old_line.r*new_line[0],old_line.alpha+new_line[1],WINDOW))
    return new_line_list
    
line_list:list[Line] = []

line_list.append(Line(100,0,WINDOW))

triangle_pattern = [[1,math.pi/3],[1,-math.pi/3],[1,math.pi]]
square_pattern = [[1,math.pi/2],[1,0],[1,-math.pi/2]]

is_running = True

while is_running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                line_list = makeLine(line_list,triangle_pattern,WINDOW)
        


    WINDOW.fill((255,255,255))
    starting_pos = [400,500]
    for line in line_list:
        starting_pos = line.draw(starting_pos)

    pygame.display.update()