import pygame

class Background():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.transform.smoothscale\
            (pygame.image.load('resorse/bg1.png'),\
             (self.screen_rect.width, self.screen_rect.height ))
        self.rect = self.image.get_rect()
    def set_background(self):
        self.screen.blit(self.image, self.rect)