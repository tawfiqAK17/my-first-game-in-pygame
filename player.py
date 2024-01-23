import pygame
from inventoryBox import Box
class Player():
    def __init__(self, screen, player, settings, ball):
        self.screen = screen
        self.settings = settings
        self.ball = ball
        self.height = 100
        self.width = 15
        self.player = 1  if player == 1 else 2
        self.image = pygame.transform.smoothscale(\
            pygame.image.load('resorse/player1.png'),(self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.centery = screen.get_height() / 2
        self.rect.centerx = 20 if player == 1 else screen.get_width() - 25

        self.can_move = True
        #self.movement_direction = 'stop'

        self.speed = 15

        self.score = 0
        self.points = 0

        self.boxes = []
        self.boxes_num = 3

        self.is_shoping = False

        self.up = pygame.K_UP if player == 2 else pygame.K_w
        self.down = pygame.K_DOWN if player == 2 else pygame.K_s
        self.right = pygame.K_RIGHT if player == 2 else pygame.K_d
        self.left = pygame.K_LEFT if player == 2 else pygame.K_a
        self.open_shope = pygame.K_DELETE if player == 2 else pygame.K_ESCAPE
        self.buy = pygame.K_RETURN if player == 2 else pygame.K_TAB
        self.box1 = pygame.K_b if player == 2 else pygame.K_a 
        self.box2 = pygame.K_n if player == 2 else pygame.K_z 
        self.box3 = pygame.K_m if player == 2 else pygame.K_x 
        self.box4 = pygame.K_j if player == 2 else pygame.K_c 
        self.box5 = pygame.K_k if player == 2 else pygame.K_v 
        self.box_character = [
                                pygame.K_b,
                                pygame.K_n, 
                                pygame.K_m, 
                                pygame.K_j, 
                                pygame.K_k
                            ] if player == 2 else [
                                pygame.K_a,
                                pygame.K_z, 
                                pygame.K_x, 
                                pygame.K_c, 
                                pygame.K_v
                            ]
        
    # add a point to the player points each second
    def update_points(self):
        if self.ball.is_moving:
            self.points += 1/self.settings.fps
    
    def draw_player(self):
        self.image = pygame.transform.smoothscale(\
            pygame.image.load('resorse/player1.png'),(self.width, self.height))
        self.rect.height = self.height
        self.screen.blit(self.image, self.rect)
