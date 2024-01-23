from os import wait
import pygame
import sys
from inventoryBox import Box

def the_menu(screen):
    stop = True
    play = pygame.transform.smoothscale(
            pygame.image.load('resorse/play.png'),
            (100, 70))
    play_rect = play.get_rect()
    play_rect.centerx = screen.get_rect().centerx
    play_rect.top = screen.get_rect().top + 250

    how_to_play = pygame.transform.smoothscale(
            pygame.image.load('resorse/how to play.png'),
            (250, 70))
    how_to_play_rect = how_to_play.get_rect()
    how_to_play_rect.centerx = screen.get_rect().centerx
    how_to_play_rect.top = screen.get_rect().top + 400
    while(stop):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] in range(play_rect.x, play_rect.right)\
                and event.pos[1] in range(play_rect.y, play_rect.bottom):
                    stop = False
                elif event.pos[0] in range(how_to_play_rect.x, how_to_play_rect.right)\
                and event.pos[1] in range(how_to_play_rect.y, how_to_play_rect.bottom):
                    how_to_play_screen(screen)
        screen.fill((112, 128, 144))
        screen.blit(play, play_rect)
        screen.blit(how_to_play, how_to_play_rect)
        pygame.display.update()

def how_to_play_screen(screen):
    how_to_play = True
    image = pygame.transform.smoothscale(
            pygame.image.load('resorse/how to play screen.png'),
            (screen.get_width(), screen.get_height()))
    while(how_to_play):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    how_to_play = False
        screen.blit(image, screen.get_rect())
        pygame.display.update()

'''------------ function that handle P1 and P2 movement----------'''
def move_player(keys, player, screen):
    if player.can_move:
        if keys[player.up]:
            if player.rect.top >= 0:
                player.rect.centery -= player.speed
                #player.movement_direction = 'up'
        elif keys[player.down]:
            if player.rect.bottom <= screen.get_height():
                player.rect.centery += player.speed
                #player.movement_direction = 'down'
'''======================================================='''

'''---------------mouve the selector border---------------'''
def select_trick(event, player, settings, shoping_screen):
    if shoping_screen.image_selected >= 0 \
        and shoping_screen.image_selected <= len(settings.tricks) - 2:
        if event.key == player.right:
            shoping_screen.image_selected += 1
            settings.tricks[shoping_screen.image_selected].is_selected = True
            for idx in range(0, shoping_screen.image_selected):
                settings.tricks[idx].is_selected = False
    if shoping_screen.image_selected >= 1 \
        and shoping_screen.image_selected <= len(settings.tricks) - 1:
        if event.key == player.left:
            shoping_screen.image_selected -= 1
            settings.tricks[shoping_screen.image_selected].is_selected = True
            for idx in range(shoping_screen.image_selected + 1, len(settings.tricks)):
                settings.tricks[idx].is_selected = False
    if shoping_screen.image_selected >= 0 \
        and shoping_screen.image_selected <= len(settings.tricks) - 5:
        if event.key == player.down:
            shoping_screen.image_selected += 4
            settings.tricks[shoping_screen.image_selected].is_selected = True
            for idx in range(0, shoping_screen.image_selected):
                settings.tricks[idx].is_selected = False
    if shoping_screen.image_selected >= 4 \
        and shoping_screen.image_selected <= len(settings.tricks) - 1:
        if event.key == player.up:
            shoping_screen.image_selected -= 4
            settings.tricks[shoping_screen.image_selected].is_selected = True
            for idx in range(shoping_screen.image_selected + 1, len(settings.tricks)):
                settings.tricks[idx].is_selected = False
    if event.key == player.buy:
        if player.points >= settings.tricks[shoping_screen.image_selected].price:
                try:
                    player.boxes.insert(player.boxes.index(None), Box(settings,settings.tricks[shoping_screen.image_selected]))
                    player.boxes.pop(player.boxes.index(None))
                except:
                    if player.boxes_num > len(player.boxes):
                        player.boxes.append(Box(settings,settings.tricks[shoping_screen.image_selected]))

                player.points -= settings.tricks[shoping_screen.image_selected].price
'''======================================================='''
''''--------------------activate the trick in the inventory'''
def activate(event, screen, player,enemy, ball):
    if not player.is_shoping:
        if event.key in player.box_character:
            if player.box_character.index(event.key) <= player.boxes_num-1:   
                if player.boxes[player.box_character.index(event.key)]:
                    if player.boxes[player.box_character.index(event.key)].activate(screen, player, enemy, ball):
                        player.boxes[(player.box_character.index(event.key))] = None 
''''======================================================'''
def check_event(settings1,settings2,screen, player1, player2, ball, shopingScreen1, shopingScreen2):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                # if event.key == pygame.K_w or event.key == pygame.K_s:
                #     player1.movement_direction = 'stop'
                # if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                #     player2.movement_direction = 'stop'
                if event.key == pygame.K_SPACE:
                    if not player1.is_shoping and not player2.is_shoping:
                        ball.is_moving = True
                        ball.is_start = True
                if ball.is_start:
                    if event.key == player1.open_shope:
                        if player2.is_shoping:
                            player1.is_shoping = True if not player1.is_shoping else False
                        else:
                            ball.is_moving = False if ball.is_moving else True
                            player1.is_shoping = True if not player1.is_shoping else False
                            player1.can_move = True if not player1.can_move else False
                            player2.can_move = True if not player2.can_move else False
                    if event.key == player2.open_shope:
                        if player1.is_shoping:
                            player2.is_shoping = True if not player2.is_shoping else False
                        else:
                            ball.is_moving = False if ball.is_moving else True
                            player2.is_shoping = True if not player2.is_shoping else False
                            player2.can_move = True if not player2.can_move else False
                            player1.can_move = True if not player1.can_move else False
                if player1.is_shoping:
                    select_trick(event, player1, settings1, shopingScreen1)
                if player2.is_shoping:
                    select_trick(event, player2, settings2, shopingScreen2)
                activate(event, screen, player1, player2, ball)
                activate(event, screen, player2, player1, ball)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        sys.exit()
        
    if not player1.is_shoping:
        move_player(keys, player1, screen)
    if not player2.is_shoping:    
        move_player(keys, player2, screen)

def screen_updating(player1, player2, ball, bg, score1, score2, inventory1, inventory2):
    bg.set_background()
    player1.draw_player()
    player2.draw_player()
    ball.ball_draw()
    ball.ball_movement(player1, player2)
    score1.display_score()
    score2.display_score()
    inventory1.draw_inventory()
    inventory2.draw_inventory()



'''returning the default values'''
def set_default(player):
    player.speed = 15
    player.height = 100

    player.up = pygame.K_UP if player.player == 2 else pygame.K_w
    player.down = pygame.K_DOWN if player.player == 2 else pygame.K_s