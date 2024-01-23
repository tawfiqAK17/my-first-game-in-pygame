import pygame
from trick import Trick

class ShopingScreen():
    def __init__(self, screen, player, settings):
        self.player = player
        self.screen = screen
        self.settings = settings
        self.image = pygame.transform.smoothscale(
            pygame.image.load('resorse/shopping.png'),
            (500, self.screen.get_height())
        )
        self.image.set_alpha(100)
        self.rect = self.image.get_rect()
        self.rect.right = screen.get_width() if player.player == 2 \
            else 500

        self.border = pygame.transform.smoothscale(
            pygame.image.load('resorse/border.png'),
            (100, 100)) 
        self.border_rect = self.border.get_rect()
        self.border_rect.left = self.rect.left + 20
        self.border_rect.top = self.rect.top + 100

        self.image_selected = 0

        self.trick_name = ''
        self.text = pygame.font.SysFont("comicsansms", 20)\
            .render(str(self.trick_name), True , (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.top = self.rect.top + 60
        self.text_rect.centerx = self.rect.centerx - 100

    def shoping(self):
        box_x_position = self.rect.left + 20
        box_y_position = self.rect.top + 100
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text, self.text_rect)
        for trick in self.settings.tricks:
            trick.rect.x = box_x_position
            trick.rect.y = box_y_position
            price_color = (255, 255, 255) \
                if self.player.points >= trick.price\
                else (204, 0, 0)
            self.screen.blit(trick.image, (box_x_position,box_y_position))
            price = pygame.font.SysFont("comicsansms", 25)\
            .render(str(int(trick.price)), True , price_color)
            price_rect = price.get_rect()
            price_rect.centerx = box_x_position + 50
            price_rect.centery = box_y_position + 120
            self.screen.blit(price, price_rect)
            box_x_position += 120
            if box_x_position >= self.rect.right - 100:
                box_y_position += 150
                box_x_position = self.rect.left + 20
            if trick.is_selected:
                trick.draw_border()
                self.trick_name = trick.trick
            self.text = pygame.font.SysFont("comicsansms", 20)\
            .render(str(self.trick_name), True , (255, 255, 255))
            self.screen.blit(self.text, self.text_rect)
            # price = pygame.font.SysFont("comicsansms", 25)\
            # .render(str(int(trick.price)), True , (0, 0, 0))
