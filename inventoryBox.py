import pygame
import functions as funs
class Box():
    def __init__(self, settings = None, trick = None):
        self.settings = settings
        self.trick = trick
        self.contain = True if self.trick else False
        if self.contain:    
            self.box = pygame.transform.smoothscale(trick.image,(50,50))
            self.rect = self.box.get_rect()
        self.border = pygame.transform.smoothscale(
            pygame.image.load(f"resorse/inventory.png"),
            (50,50))
        self.border_rect = self.border.get_rect()

    def activate(self,screen, player, enemy, ball):
        if self.trick == self.settings.tricks[0]:
                ball.x_speed = ball.x_speed * 5
                ball.y_speed = ball.y_speed * 5
                return True

        elif self.trick == self.settings.tricks[1]:
            if player.height < 200:
                player.height += 100
                if player.rect.top == player.screen.get_rect().top:
                    player.rect.y += 10
                if player.rect.bottom == player.screen.get_height():
                    player.rect.y -= 10
                return True
            else:
                screen.blit(pygame.font.SysFont("comicsansms", 30)\
                .render('Max lenght', True , (0, 0, 0)),(screen.get_width()/2, screen.get_height() - 50))
            return False

        elif self.trick == self.settings.tricks[2]:
            if enemy.height > 50:
                enemy.height -= 10
            return True

        elif self.trick == self.settings.tricks[3]:
            if player.boxes_num < 5:
                player.boxes_num += 1
            return True

        elif self.trick == self.settings.tricks[4]:
            ball.x_speed = - ball.x_speed
            return True

        elif self.trick == self.settings.tricks[5]:
            enemy.up, enemy.down = enemy.down, enemy.up
            return True

        elif self.trick == self.settings.tricks[6]:
            funs.set_default(player)
            return True


    
