import random
from CONSTANTS import *
class Unit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inventory = []
    def move(self, direct):
        match direct:
            case 'up':
                self.y -= 1
            case 'down':
                self.y += 1
            case 'right':
                self.x += 1
            case 'left':
                self.x -= 1
    # def move_up(self):
    #     self.y -= 1
    # def move_down(self):
    #     self.y += 1
    # def move_right(self):
    #     self.x += 1
    # def move_left(self):
    #     self.x -= 1
    #
    # def random_walk(self):
    #     if random.random() > 0.9:
    #         self.x += random.randint(-1, 1)
    #         self.y += random.randint(-1, 1)
    #         self.x = max(0, min(self.x, GRID_WIDTH - 1))
    #         self.y = max(0, min(self.y, GRID_HEIGHT - 1))