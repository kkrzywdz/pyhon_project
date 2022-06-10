import os
import time


class Gear:
    def __init__(self, gears):
        self.gear = gears
        self.obwod = gears * 6
        self.r = gears
        self.x = 0
        self.y = 0
        self.z = 0
        self.rot = 0
        self.step = 360/gears
        self.nextGear = [];

    def set_poz (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_poz(self):
        return self.x, self.y, self.z

    def connect_gear(self, ngear):
        self.nextGear = ngear

    def rotate_steps(self, steps, direction):
        dif = self.step * steps * direction
        self.rot += dif
        if self.rot < 0:
            self.rot += 360
        if self.rot >= 360:
            self.rot -= 360
        return dif

    def rotate_rot(self, dif, direction):
        self.rot += dif
        if self.rot < 0:
            self.rot += 360
        if self.rot >= 360:
            self.rot -= 360
        return 360/self.gear*dif


g1 = Gear(8)
g2 = Gear(16)
g3 = Gear(4)
g4 = Gear(16)

for step in range(1000):
    os.system('cls')
    print("step:" + str(step))
    print("g1:" + str(g1.rot))
    print("g2:" + str(g2.rot))
    print("g3:" + str(g3.rot))
    print("g4:" + str(g4.rot))
    g1.rotate_steps(1, 1)
    g2.rotate_steps(1, -1)
    g3.rotate_steps(1, 1)
    g4.rotate_steps(1, -1)
    time.sleep(0.1)


def print_name_of_gear(name: object) -> object:
    print("name")

print_name_of_gear('1')