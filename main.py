import pygame
from sys import exit
from Sprites import *
from Settings import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

outer_circle = OuterCircle()
all_sprites = pygame.sprite.Group()
all_sprites.add(outer_circle)

ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
all_sprites.add(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(60)
