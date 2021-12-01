import pygame, sys, random
from pygame.math import Vector2


class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_size-1)
        self.y = random.randint(0,cell_size-1)
        self.pos = Vector2(self.x,self.y)
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size ,cell_size,cell_size)
        pygame.draw.rect(screen,('Red'),fruit_rect)
    
#class SNAKE: 
 #   def __init__(self):
   #     self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
      #  def draw_snake(self):

    
pygame.init()
cell_size = 20
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
#test_surface = pygame.Surface((100,200))

fruit = FRUIT()

while True: 
    for event in pygame.event.get(): #gets event
        if event.type == pygame.QUIT: #if statement for event and makes a QUIT function
            pygame.quit() #calls the function
            sys.exit()
    screen.fill(pygame.Color('Gray'))
    fruit.draw_fruit()
    #screen.blit(test_surface,(200,250))
    #test_surface.fill(pygame.Color('Blue'))
    pygame.display.update()
    clock.tick(100)
    