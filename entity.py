import pygame

class Sun:
    def __init__(self, pos_x, pos_y, scrx, scry):
        self.x = pos_x
        self.y = pos_y
        self.img = pygame.image.load("images/Sun_PvZ2.png")
        self.scrx = scrx
        self.scry = scry
        self.img = pygame.transform.scale(self.img, [scrx/21,scry/15])

    def sunappear(self, screen):
        screen.blit(self.img, [self.x, self.y])

    def sunclick(self, click):
        if self.x <= click[0] <= self.x + self.scrx/21 and self.y <= click[1] <= self.y + self.scry/15:
            return True
