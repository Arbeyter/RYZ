import pygame
import random, time
import units
import os

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Размеры экрана
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Размеры клетки
CELL_SIZE = 40

class Tile:
    def __init__(self):
        self.passable = random.choices([True, False], [0.9, 0.1])[0]
        self.objects = []

    def append(self, obj):
        self.objects.append(obj)

    def remove(self, obj):
        self.objects.remove(obj)


class Location:
    def __init__(self, rows, cols):
        self.N = rows
        self.M = cols
        self.location = [[Tile() for i in range(self.N)] for j in range(self.M)]
    def __getitem__(self, item):
        return self.location[item]
    def check_step(self, x, y, ):
        if (x < 0) or (y < 0):
            return False
        if (x >= self.N) or (y >= self.M):
            return False
        if self.location[x][y].passable:
            return True
        return False
    # def move(self, obj, x,y,):
    def printer(self):
        for i in range(self.M):
            for j in range(self.N):
                if self.location[i][j].objects:
                    print('*',end='')
                else:
                    if self.location[i][j].passable:
                        print('0',end='')
                    else:
                        print('1',end='')
            print()

    def draw(self, screen):
        for i in range(self.M):
            for j in range(self.N):
                color = WHITE if self.location[i][j].passable else BLACK
                pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                if self.location[i][j].objects:
                    pygame.draw.circle(screen, GREEN, (j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 4)
class Harvest_Manager:
    def __init__(self, location):
        self.list_unit = []
        self.location = location

    def append(self, obj):
        self.list_unit.append(obj)

    def harvest(self, receiver, donor):
        #не ебу че тут сделать, ведь ресурсы разные могут быть, плюс у юнитов есть инвентарь свой и ограничение по весу
        if donor.capacity >0:
            donor.capacity -= 1
            #receiver.
class Move_Manager:
    def __init__(self, location):
        self.list_unit = []
        self.location = location

    def append(self, obj):
        self.list_unit.append(obj)

    def move_obj(self, obj, direct):
        tmpx, tmpy = obj.x, obj.y
        match direct:
            case 'up':
                tmpy -= 1
            case 'down':
                tmpy += 1
            case 'right':
                tmpx += 1
            case 'left':
                tmpx -= 1
        if self.location.check_step(tmpy, tmpx):
            x, y, = obj.x, obj.y
            self.location[y][x].remove(obj)
            self.location[tmpy][tmpx].append(obj)
            obj.move(direct)

    def move_AI(self):
        pass

class Player_Manager:
    pass

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# Создание объектов
gameboard = Location(10, 10)
manager = Move_Manager(gameboard)
u = units.Unit(0, 0)
gameboard.location[0][0].append(u)

# Главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            #k = None
            if event.key == pygame.K_LEFT:
                manager.move_obj(u, 'left')
            if event.key == pygame.K_RIGHT:
                manager.move_obj(u, 'right')
            if event.key == pygame.K_UP:
                manager.move_obj(u, 'up')
            if event.key == pygame.K_DOWN:
                manager.move_obj(u, 'down')
    # Движение юнита случайным образом
    #manager.move_obj(u, random.choices(['up', 'left', 'down', 'right'],[0.2,0.2,0.3,0.3])[0])

    # Отрисовка
    screen.fill(BLACK)
    gameboard.draw(screen)
    pygame.display.flip()

    #time.sleep(0.5)

pygame.quit()