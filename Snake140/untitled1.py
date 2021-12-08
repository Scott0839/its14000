# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:54:47 2021

@author: Richard
"""

import pygame, sys, random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
        
        self.head = pygame.image.load('Graphics/S.png')
        self.neck = pygame.image.load('Graphics/N.png')
        self.body1 = pygame.image.load('Graphics/A.png')
        self.body2 = pygame.image.load('Graphics/K.png')
        self.tail = pygame.image.load('Graphics/E.png')
        self.hyp = pygame.image.load('Graphics/Hyp.png')
        self.tail1 = pygame.image.load('Graphics/G.png')
        self.tail2 = pygame.image.load('Graphics/A.png')
        self.tail3 = pygame.image.load('Graphics/M.png')
        self.tail4 = pygame.image.load('Graphics/E.png')
        
        
        
    def draw_snake(self):
        
        for index,block in enumerate(self.body):
            #create a rectangle
            #draw the rectangle
            x_pos = int(block.x * cell_size) #here we're making it so that the block_rect code isn't so long
            y_pos = int(block.y * cell_size) #these determine x and y values of snake and make them cell-sized
            block_rect = pygame.Rect(x_pos,y_pos,cell_size, cell_size) 
            
            if index == 0:
                    screen.blit(self.head,block_rect)
            elif index == 1:
                screen.blit(self.neck,block_rect)
            elif index == 2:
                screen.blit(self.body1,block_rect)
            elif index == 3:
                screen.blit(self.body2,block_rect)
            elif index == 4:
                screen.blit(self.tail,block_rect)
            elif index == 5:
                screen.blit(self.hyp,block_rect)    
            elif index == 6:
               screen.blit(self.tail1,block_rect)   
            elif index == 7:
                screen.blit(self.tail2,block_rect) 
            elif index == 8:
                screen.blit(self.tail3,block_rect) 
            elif index == 9:
                screen.blit(self.tail4,block_rect)    
            else: 
                pygame.draw.rect(screen,(150,100,100),block_rect)
            
            
            
            
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
        screen.blit(orange, fruit_rect)
        
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
        self.check_fail() #call checkfail below
    def draw_elements(self):
        self.fruit.draw_fruit() #this draws the fruit that we made in class FRUIT
        self.snake.draw_snake()
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:   #if fruit is in the same space as the snake head
            #reposition the fruit and add another block to the snake
            self.fruit.randomize()
            self.snake.add_block()
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number: #ends game if snake is to far to the left or right
          self.game_over()  
          
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game(over)
        #check if snake hits itself

    def game_over(self):
        pygame.quit()
        sys.exit()
    #def draw_elements(self) #59:30
pygame.init()
cell_size = 20
cell_number = 40
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
orange = pygame.image.load('Graphics/orange.png')


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
                if main_game.snake.direction.y !=1:#only allows you to move left/right if you arent going to collide with yourself
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x !=-1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y !=-1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x !=1:
                    main_game.snake.direction = Vector2(-1, 0)        
            
    screen.fill(pygame.Color('Gray'))
    
    #screen.blit(test_surface,(200,250))
    #test_surface.fill(pygame.Color('Blue'))
    
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)