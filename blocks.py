import pygame
import random, math


class Block:
    def __init__(self, x, y):
        self.x = 0
        self.y = 0
        self.color = (255, 255, 255)
        self.capacity = 20

    def draw(self):
        return self.color

    def harvest(self):
        pass
