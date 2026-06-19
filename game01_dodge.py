import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
player_x = 380
player_y = 520

# 敵2体が別の場所から落ち始めるように、それぞれの座標を用意する
enemy1_x = 200
enemy1_y = 0
enemy2_x = 560
enemy2_y = -300
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
                player_x = 380
                player_y = 520
                # リスタートするときは、敵2体も上の別々の位置に戻す
                enemy1_x = random.randint(0, 760)
                enemy1_y = 0
                enemy2_x = random.randint(0, 760)
                enemy2_y = -300
                score = 0
                game_over = False
    
    keys = pygame.key.get_pressed()

    if not game_over:
        if keys[pygame.K_LEFT]:
            player_x -= 0.5

        if keys[pygame.K_RIGHT]:
            player_x += 0.5

    if not game_over:
        # ゲーム中は敵2体を同じ速さで下に動かす
        enemy1_y += 0.5
        enemy2_y += 0.5
        score += 0.01

    # 画面の下まで進んだ敵は、横位置を変えて上から落とし直す
    if enemy1_y > 600:
        enemy1_y = 0
        enemy1_x = random.randint(0, 760)

    if enemy2_y > 600:
        enemy2_y = 0
        enemy2_x = random.randint(0, 760)

    # 敵1か敵2のどちらかに当たったらゲームオーバーにする
    hit_enemy1 = (
        player_x < enemy1_x + 40
        and player_x + 40 > enemy1_x
        and player_y < enemy1_y + 40
        and player_y + 40 > enemy1_y
    )
    hit_enemy2 = (
        player_x < enemy2_x + 40
        and player_x + 40 > enemy2_x
        and player_y < enemy2_y + 40
        and player_y + 40 > enemy2_y
    )

    if hit_enemy1 or hit_enemy2:
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

        restart_text = font.render(
            "Press R to Restart",
            True,
            (255, 255, 255)
        )

        screen.blit(restart_text, (150, 330))

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (player_x, player_y, 40, 40)
    )

    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (enemy1_x, enemy1_y, 40, 40)
    )

    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (enemy2_x, enemy2_y, 40, 40)
    )

    pygame.display.flip()
