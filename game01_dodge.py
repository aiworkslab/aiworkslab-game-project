import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
player_x = 380
player_y = 520

enemy_x = 400
enemy_y = 0
score = 0

pygame.display.set_caption("Game 01 Dodge")

font = pygame.font.SysFont(None, 72)

running = True

game_over = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                player_x == 300
                player_y == 520
                enemy_x = random.randint(0, 760)
                enemy_y = 0
                score = 0
                game_over = False
    
    keys = pygame.key.get_pressed()

    if not game_over:
        if keys[pygame.K_LEFT]:
            player_x -= 0.5

        if keys[pygame.K_RIGHT]:
            player_x += 0.5

    if not game_over:
        enemy_y += 0.5
        score += 0.01
        
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
        game_over = True

    screen.fill((0, 0, 0))

    score_text = font.render(
        f"SCORE : {int(score)}",
        True,
        (255, 255, 255)
    )

    screen.blit(score_text, (10, 10))

    if game_over:
        text = font.render("GAME OVER", True, (255,255,255))
        screen.blit(text, (220, 250))

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
