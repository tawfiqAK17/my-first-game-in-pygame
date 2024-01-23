import pygame

class Trick():
    def __init__(self, trick, price, screen, is_selected = False):
        self.screen = screen
        self.trick = trick
        self.border = pygame.transform.smoothscale(
            pygame.image.load('resorse/border.png'),
            (100, 100)) 
        self.image = pygame.transform.smoothscale(
            pygame.image.load(f"resorse/tricks/{self.trick}.png"),
            (100, 100))
        self.price = price
        self.is_selected = is_selected
        self.rect = self.image.get_rect()
    def draw_border(self):
            self.screen.blit(self.border, self.rect)