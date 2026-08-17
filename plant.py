import pygame

class Plant:
    def __init__(self, screen, screen_x, screen_y, plant, sungive, pos_x, pos_y, row, time, time2, hp):
        self.self = self
        self.screen = screen
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.plant = plant
        self.sungive = sungive
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.row = row
        self.time = time
        self.time2 = time2
        self.hp = hp
        self.rect = pygame.Rect(pos_x, pos_y, screen_x/17, screen_y/12)

    def appear(self, img):
        self.screen.blit(img, [self.pos_x, self.pos_y])