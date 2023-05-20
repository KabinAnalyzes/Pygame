import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("A NapN RPG")
clock = pygame.time.Clock()

bg_surface = pygame.image.load("graphics/bg.png").convert()
player_surface = pygame.image.load("graphics/player.png").convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(bg_surface,(0,0))
    screen.blit(player_surface,(80,200))
    
    pygame.display.update()
    clock.tick(60)