from more_itertools import is_sorted
import pygame
import random

class Ball():
    def __init__(self, screen, settings):
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #self.movement_direction = 'stop'
        self.ball_speed = 18
        self.x_speed = random.choice([5,-5])
        self.y_speed = random.choice([-7,7])
        self.is_moving = False
        self.is_start = False

        #set the image
        self.image = pygame.transform.smoothscale(
            pygame.image.load('resorse/ball1.png'),
            (settings.ball_size, settings.ball_size))
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.text = pygame.font.SysFont("comicsansms", 20)\
            .render(('Press SPACE to start'), True , (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center
        self.text_rect.y = self.rect.y + 100
    #function that handle the ball movement
    def ball_movement(self, player1, player2):
        if self.is_moving:
            self.rect.centerx += self.x_speed
            self.rect.centery -= self.y_speed

        if self.rect.colliderect(player1.rect) or self.rect.colliderect(player2.rect):
            self.handle_paddle_collision(player1 if self.rect.colliderect(player1.rect) else player2)
        # mack shure that the ball does not get out of the screen
        elif self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.bottom:
            self.y_speed = -self.y_speed
        # if the ball touch one of the sides it returne to the center 
        elif self.rect.centerx <= self.screen_rect.left :
            self.rect.center = self.screen_rect.center
            self.set_default_ball_speed()
            self.is_start = False
            self.is_moving = False
            player2.score += 1
            player1.points = 0
        elif self.rect.centerx >= self.screen_rect.right:
            self.rect.center = self.screen_rect.center
            self.set_default_ball_speed()
            self.is_start = False
            self.is_moving = False
            player1.score += 1
            player2.points = 0
    # you can see
    def handle_paddle_collision(self, player):
        if player.player == 1:
             self.x_speed = random.randint(16,18)
             self.y_speed = random.choice([-1, 1]) * random.randint(1,8)
        if player.player == 2:
             self.x_speed = -random.randint(16,18)
             self.y_speed = random.choice([-1, 1]) * random.randint(1,8)
        # self.movement_direction = 'up' if self.y_speed > 0 else 'down'
        # if player.movement_direction == 'stop':
        #     self.x_speed = -self.x_speed
        # elif player.movement_direction == 'up':
        #     if self.movement_direction == 'up':
        #         self.x_speed = -self.x_speed
        #         if self.y_speed <= 10:
        #             self.y_speed += int(abs(player.speed)/3)
        #     else:
        #         self.x_speed = -self.x_speed
        #         self.y_speed += int(abs(player.speed)/3)
        # else:
        #     if self.movement_direction == 'up':
        #         self.x_speed = -self.x_speed
        #         self.y_speed -= int(abs(player.speed)/3)
        #     else:
        #         self.x_speed = -self.x_speed
        #         self.y_speed -= int(abs(player.speed)/3)
        # if abs(self.x_speed)  + abs(self.y_speed) > self.ball_speed:
        #     self.x_speed = self.ball_speed - abs(self.y_speed)
        # else:
        #     self.x_speed = 7
             
    def set_default_ball_speed(self):
            self.x_speed = random.choice([5,-5])
            self.y_speed = random.choice([-7,7])
    def ball_draw(self):
        self.screen.blit(self.image, self.rect)
        if not self.is_start:
            self.screen.blit(self.text, self.text_rect)
