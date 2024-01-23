import pygame
from inventoryBox import Box
class Inventory():
    def __init__(self,screen, player):
        self.player = player
        self.screen = screen
        self.boxes = player.boxes
    def draw_inventory(self):
        last_box_right = self.screen.get_rect().centerx/2 \
            if self.player.player == 1 \
            else self.screen.get_rect().centerx/2 + self.screen.get_rect().centerx
        for i in range(0, self.player.boxes_num):
            box = Box()
            box.border_rect.bottom = self.screen.get_height()
            box.border_rect.right = last_box_right
            self.screen.blit(box.border, box.border_rect)
            last_box_right += 55
        last_box_right = self.screen.get_rect().centerx/2 \
            if self.player.player == 1 \
            else self.screen.get_rect().centerx/2 + self.screen.get_rect().centerx
        for box in self.player.boxes:
            if box == None:
                last_box_right += 55
            elif box.contain:
                box.rect.bottom = self.screen.get_height()
                box.rect.right = last_box_right
                self.screen.blit(box.box, box.rect)
                last_box_right += 55
        self.boxes = self.player.boxes
       