import pygame, sys, random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
    def draw_snake(self):
        
        for block in self.body:
            #create a rectangle
            #draw the rectangle
            x_pos = int(block.x * cell_size) #here we're making it so that the block_rect code isn't so long
            y_pos = int(block.y * cell_size) #these determine x and y values of snake and make them cell-sized
            block_rect = pygame.Rect(x_pos,y_pos,cell_size, cell_size) 
            pygame.draw.rect(screen,('green'), block_rect) #draws the snake
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else: 
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
           
    def add_block(self):         
        self.new_block = True

class FRUIT:
    def __init__(self):
        self.randomize()
        #self.x = random.randint(0,cell_size-1) 
        #self.y = random.randint(0,cell_size-1)
        #self.pos = Vector2(self.x,self.y) All of these were replaced by self.randomize
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size ,cell_size,cell_size)
        pygame.draw.rect(screen,('Red'),fruit_rect)
        
    def randomize(self):
        self.x = random.randint(0,cell_size-1)
        self.y = random.randint(0,cell_size-1)
        self.pos = Vector2(self.x,self.y)
        #this code is the same as the initialize code, except it is only activated when the check collision function activates it
    
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        
    def update(self):
        self.snake.move_snake() #calls the move_snake command from the snake class
        self.check_collision() # calls the check collision function to make snake eating the fruit count
    def draw_elements(self):
        self.fruit.draw_fruit() #this draws the fruit that we made in class FRUIT
        self.snake.draw_snake()
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:   #if fruit is in the same space as the snake head
            #reposition the fruit and add another block to the snake
            self.fruit.randomize()
            self.snake.add_block()

    #def draw_elements(self) #59:30
pygame.init()
cell_size = 20
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
#test_surface = pygame.Surface((100,200))


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
main_game = MAIN()


fruit = FRUIT() #makes the class FRUIT = the variable fruit then uses it in the while main game loop
snake = SNAKE()
while True: 
    for event in pygame.event.get(): #gets event
        if event.type == pygame.QUIT: #if statement for event and makes a QUIT function
            pygame.quit() #calls the function
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0)        
            
    screen.fill(pygame.Color('Gray'))
    
    #screen.blit(test_surface,(200,250))
    #test_surface.fill(pygame.Color('Blue'))
    
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
    