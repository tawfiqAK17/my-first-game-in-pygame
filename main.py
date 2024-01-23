import pygame
import functions as funs
from settings import Settings
from player import Player
from ball import Ball
from background import Background
from score import Score
from inventory import Inventory
from shopingScreen import ShopingScreen

screen = pygame.display.set_mode((1800,800))
clock = pygame.time.Clock()
def main():
    pygame.init()
    settings1 = Settings(screen)
    settings2 = Settings(screen)
    ball = Ball(screen, settings1)
    player1 = Player(screen, 1, settings1, ball)
    player2 = Player(screen, 2, settings2, ball)
    bg = Background(screen)
    score2 = Score(screen, player2)
    inventory1 = Inventory(screen, player1)
    inventory2 = Inventory(screen, player2)
    shoping_screen1 = ShopingScreen(screen, player1, settings1)
    shoping_screen2 = ShopingScreen(screen, player2, settings2)
    funs.the_menu(screen)
    while(True):
        clock.tick(settings1.fps)
        # I creat the score instances inside the loop to update 
        # the score each time
        score1 = Score(screen, player1)
        score2 = Score(screen, player2)
        funs.screen_updating(player1, player2, ball, bg, score1, score2, inventory1, inventory2)
        player1.update_points()
        player2.update_points()
        inventory1.draw_inventory()
        inventory2.draw_inventory()
        if player1.is_shoping:
            shoping_screen1.shoping()
        if player2.is_shoping:
            shoping_screen2.shoping()
        funs.check_event(settings1,settings2, screen, player1, player2, ball, shoping_screen1, shoping_screen2)
        pygame.display.update()
        
        

            
main()