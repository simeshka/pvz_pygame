import pygame
import random

class Enemy:
    def __init__(self, hp, speed, screen, pos_x, pos_y, size_x, size_y, zrng):
        self.hp = hp
        self.speed = speed
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.zrng = zrng
        self.rect = pygame.Rect(self.pos_x, self.pos_y, size_x, size_y)

    def appear(self, img):
        self.screen.blit(img, [self.pos_x, self.pos_y])

    def rectdraw(self, color):
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.size_x, self.size_y)
        pygame.draw.rect(self.screen, color, self.rect)


