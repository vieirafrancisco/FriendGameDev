import pygame
from time import sleep
from config import *
from ball import Ball 
from player import Player

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

ball = Ball(7, FPS, SPEED_BALL, 300, 300)
player1 = Player(20, int(HEIGHT/2 - 60/2), 150, FPS, PLAYER1_KEYS)
player2 = Player(WIDTH-20, int(HEIGHT/2 - 60/2), 150, FPS, PLAYER2_KEYS)

def wall_collision():
    r = ball.out_off_screen()
    if r == 1:
        player1.score+=1
    if r == -1:
        player2.score+=1      

def update():
    ball.update()
    ball.collision(player1.rect)
    ball.collision(player2.rect)
    player1.update(pygame.key.get_pressed())
    player2.update(pygame.key.get_pressed())
    wall_collision()
    print(player1.score, player2.score)

def render():
    player1.draw(screen)
    player2.draw(screen)
    ball.draw(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
     
    screen.fill((0,0,0))

    update()
    render()    

    pygame.display.flip()
    clock.tick(FPS)
    

    
    