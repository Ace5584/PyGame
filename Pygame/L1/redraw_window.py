import pygame

clock = pygame.time.Clock()  # clock
bg = pygame.image.load('background/bg.jpg')  # Importing background image
font = pygame.font.SysFont('comicsans', 60)
shield_timer_font = pygame.font.SysFont('comicsans', 15)

shield_timer = [pygame.image.load('timer/timer_1.png'), pygame.image.load('timer/timer_2.png'),
                pygame.image.load('timer/timer_3.png'), pygame.image.load('timer/timer_4.png')]


def redraw_window(window, player1, player2, screen_x, time_seconds, bullet_seconds, pause=False, start_screen=False):
    clock.tick(60)
    window.blit(bg, (0, 0))
    window.blit(player1.player_information, player1.text_location)
    window.blit(player2.player_information, player2.text_location)
    window.blit(player1.player_bullet_count, player1.bullet_count_text_location)
    window.blit(player2.player_bullet_count, player2.bullet_count_text_location)
    for z in player1.bullets:
        z.shoot_bullet(window, 'red')
    for z in player2.bullets:
        z.shoot_bullet(window, 'blue')

    pygame.draw.rect(window, (255, 255, 255), player1.bottom_health_bar_location)
    pygame.draw.rect(window, (255, 255, 255), player2.bottom_health_bar_location)
    pygame.draw.rect(window, (255, 0, 0), player1.health_bar_location)
    pygame.draw.rect(window, (255, 0, 0), player2.health_bar_location)
    pygame.draw.rect(window, (255, 255, 255), player1.bottom_shield_bar)
    pygame.draw.rect(window, (255, 255, 255), player2.bottom_shield_bar)
    pygame.draw.rect(window, (0, 0, 255), player1.shield_bar)
    pygame.draw.rect(window, (0, 0, 255), player2.shield_bar)
    if bullet_seconds == 0:
        window.blit(shield_timer[3], player1.shield_timer_location)
        window.blit(shield_timer[3], player2.shield_timer_location)
    if bullet_seconds == 1 or bullet_seconds == 2 or bullet_seconds == 3:
        window.blit(shield_timer[2], player1.shield_timer_location)
        window.blit(shield_timer[2], player2.shield_timer_location)
    if bullet_seconds == 4 or bullet_seconds == 5 or bullet_seconds == 6:
        window.blit(shield_timer[1], player1.shield_timer_location)
        window.blit(shield_timer[1], player2.shield_timer_location)
    if bullet_seconds == 7 or bullet_seconds == 8 or bullet_seconds == 9:
        window.blit(shield_timer[0], player1.shield_timer_location)
        window.blit(shield_timer[0], player2.shield_timer_location)

    if not pause:
        text = font.render(str(time_seconds), True, (255, 255, 255))
        window.blit(text, (screen_x / 2 - text.get_width() / 2, 0))
        player1.draw(window, 1)
        player2.draw(window, 2)
        player1.attack(player2, window)
        player2.attack(player1, window)
        pygame.display.update()
    else:
        if start_screen:
            player1.freeze(window, 1)
            player2.freeze(window, 2)
        else:
            if player1.is_dead():
                player1.freeze(window, 1)
            else:
                player2.freeze(window, 2)
