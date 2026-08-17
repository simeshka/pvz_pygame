import pygame
import random

class Enemy:
    def __init__(self, hp: int, speed: int, screen, pos_x: int, pos_y: int, size_x: int, size_y: int, zrng: int, iseat: bool, eating):
        self.hp = hp
        self.speed = speed
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.zrng = zrng
        self.rect = pygame.Rect(self.pos_x, self.pos_y+15, size_x, size_y)
        self.iseat = iseat
        self.eating = eating

    def appear(self, img):
        self.screen.blit(img, [self.pos_x, self.pos_y])

    def rectdraw(self, color):
        self.rect = pygame.Rect(self.pos_x+40, self.pos_y+15, self.size_x, self.size_y)
        pygame.draw.rect(self.screen, color, self.rect)


