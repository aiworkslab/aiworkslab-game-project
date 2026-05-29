import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
player_x = 380
player_y = 520

pygame.display.set_caption("Game 01 Dodge")

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= 0.5

    if keys[pygame.K_RIGHT]:
        player_x += 0.5

    screen.fill((0, 0, 0))

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (player_x, player_y, 40, 40)
    )

    pygame.display.flip()