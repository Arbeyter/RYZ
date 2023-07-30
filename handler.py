import random, time
import units
import os

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
        if (x > self.N) or (y > self.M):
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


class Harvest_Manager:
    def __init__(self, location):
        self.list_unit = []
        self.location = location

    def append(self, obj):
        self.list_unit.append(obj)

    def harvest(self, receiver, donor):
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
        if self.location.check_step(tmpx, tmpy):
            x, y, = obj.x, obj.y
            self.location[x][y].remove(obj)
            self.location[tmpx][tmpy].append(obj)
            obj.move(direct)

    def move_AI(self):
        pass


if __name__ == '__main__':
    gameboard = Location(20,10)
    manager = Move_Manager(gameboard)
    u = units.Unit(0,0)
    gameboard.location[0][0].append(u)
    while True:
        manager.move_obj(u, random.choice(['up','left','down','right']))

        gameboard.printer()
        time.sleep(0.5)
        os.system('cls')
