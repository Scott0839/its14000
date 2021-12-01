import pygame, sys, random


class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_size-1)
        self.y = random.randint(0,cell_size-1)
        self.pos = Vector2(self.x,self.y)
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x)
#around 36 minutes into vid


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200))

while True: 
    for event in pygame.event.get(): #gets event
        if event.type == pygame.QUIT: #if statement for event and makes a QUIT function
            pygame.quit() #calls the function
            sys.exit()
    screen.fill(pygame.Color('Red'))
    screen.blit(test_surface,(200,250))
    test_surface.fill(pygame.Color('Blue'))
    pygame.display.update()
    clock.tick(100)
    