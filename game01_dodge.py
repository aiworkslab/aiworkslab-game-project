import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
player_x = 380
player_y = 520

enemy_x = 400
enemy_y = 0

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

    enemy_y += 0.5
    
    if enemy_y > 600:
        enemy_y = 0
        enemy_x = random.randint(0, 760)

    if (
        player_x < enemy_x + 40
        and player_x + 40 > enemy_x
        and player_y < enemy_y + 40
        and player_y + 40 > enemy_y
    ):
        print("ゲームオーバー")
        running = False

    screen.fill((0, 0, 0))

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (player_x, player_y, 40, 40)
    )

    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (enemy_x, enemy_y, 40, 40)
    )

    pygame.display.flip()
