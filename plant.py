class Plant:
    def __init__(self, screen, plant, sungive, pos_x, pos_y, row, time):
        self.self = self
        self.screen = screen
        self.plant = plant
        self.sungive = sungive
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.row = row
        self.time = time

    def appear(self, img):
        self.screen.blit(img, [self.pos_x, self.pos_y])