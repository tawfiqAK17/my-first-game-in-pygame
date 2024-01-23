import pygame

class Score():
    SCORE_SIZE = 80
    POINTS_SIZE = 40

    def __init__(self, screen, player):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.score_size = Score.SCORE_SIZE
        self.points_size = Score.POINTS_SIZE

        self.score_text = pygame.font.SysFont("comicsansms", self.score_size)\
            .render(str(player.score), True , (0, 0, 0))
        self.points_text = pygame.font.SysFont("comicsansms", self.points_size)\
            .render("points: " + str(int(player.points)), True , (0, 0, 0))
        self.score_text_rect = self.score_text.get_rect()
        self.points_text_rect = self.points_text.get_rect()
        if player.player == 1:
            self.score_text_rect.centerx = self.screen_rect.centerx - 100
            self.points_text_rect.centerx = self.screen_rect.centerx - 500
        else:
            self.score_text_rect.centerx = self.screen_rect.centerx + 100
            self.points_text_rect.centerx = self.screen_rect.centerx + 500
    def display_score(self):
        self.screen.blit(self.score_text, self.score_text_rect)
        self.screen.blit(self.points_text, self.points_text_rect)
