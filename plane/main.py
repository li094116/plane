import random
import time

import pygame
from pygame.locals import *
# create a window

screen = pygame.display.set_mode((480, 700), 0, 32)
bg_image1 = pygame.image.load("images/background.png")
bg_image2 = pygame.image.load("images/background.png")
plane_image = pygame.image.load("images/me1.png")
other_plane = pygame.image.load("images/enemy1.png")
game_over = pygame.image.load("images/gameover.png")

FPS = 300# 初始化游戏难度
FPSClock = pygame.time.Clock()

# 飞机初始坐标
x = 200
y = 600

# 背景滚动
by1 = 0
by2 = -700

enemy_group = [] # 小飞机
big_enemy_group = [] # 中飞机
s_enemy_group = []  # 大飞机

# 飞机血条
count_bigplane_blood = 0
count_splane_blood = 0

# 计分器
score = 0
class BasePlane():
    def __init__(self, screen, x, y, image_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.speed = 1
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))



class MyPlane(BasePlane):
    def __init__(self, screen, x, y, image_filename, image2_filename):
        BasePlane.__init__(self, screen, x, y, image_filename)
        self.image2 = pygame.image.load(image2_filename)
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.bullet = []
        global enemy_group
        self.enemy_group = enemy_group
        global count_bigplane_blood
        self.count_bigplane_blood = count_bigplane_blood
        global big_enemy_group
        self.big_enemy_group = big_enemy_group
        global s_enemy_group
        self.s_enemy_group = s_enemy_group
        global count_splane_blood
        self.count_splane_blood = count_splane_blood
        self.plane_died1 = pygame.image.load("images/enemy1_down1.png")
        self.plane_died2 = pygame.image.load("images/enemy1_down2.png")
        self.plane_died3 = pygame.image.load("images/enemy1_down3.png")
        self.plane_died4 = pygame.image.load("images/enemy1_down4.png")

        self.plane_big_died1 = pygame.image.load("images/enemy3_down1.png")
        self.plane_big_died2 = pygame.image.load("images/enemy3_down2.png")
        self.plane_big_died3 = pygame.image.load("images/enemy3_down3.png")
        self.plane_big_died4 = pygame.image.load("images/enemy3_down4.png")
        self.plane_big_died5 = pygame.image.load("images/enemy3_down5.png")
        self.plane_big_died6 = pygame.image.load("images/enemy3_down6.png")

        self.plane_died_s1 = pygame.image.load("images/enemy2_down1.png")
        self.plane_died_s2 = pygame.image.load("images/enemy2_down2.png")
        self.plane_died_s3 = pygame.image.load("images/enemy2_down3.png")
        self.plane_died_s4 = pygame.image.load("images/enemy2_down4.png")
    def display(self):
        self.image_choice = random.choice([self.image, self.image2])
        self.screen.blit(self.image_choice, (self.x, self.y))
        global score
        for bullet in self.bullet:
            bullet.display()
            bullet.move()
            if bullet.out_of_rangebu():
                self.bullet.remove(bullet)
            for i in self.enemy_group:
                if (bullet.x >= i.x  and bullet.x <= i.x+57) and (bullet.y >= i.y and bullet.y <= i.y+43):
                    try:
                        self.bullet.remove(bullet)
                    except ValueError:
                        pass
                    other.boom = True
                    self.screen.blit(self.plane_died1, (i.x, i.y))
                    self.screen.blit(self.plane_died2, (i.x, i.y))
                    self.screen.blit(self.plane_died3, (i.x, i.y))
                    self.screen.blit(self.plane_died4, (i.x, i.y))
                    self.enemy_group.remove(i)
                    score += 1
                    print("score:", score)
            for i in self.big_enemy_group:
                if (bullet.x >= i.x and bullet.x <= i.x + 169) and (bullet.y >= i.y and bullet.y <= i.y + 258):
                    self.count_bigplane_blood += 1
                    self.bullet.remove(bullet)
                    if(self.count_bigplane_blood == 10):
                        self.screen.blit(self.plane_big_died1, (i.x, i.y))
                        self.screen.blit(self.plane_big_died2, (i.x, i.y))
                        self.screen.blit(self.plane_big_died3, (i.x, i.y))
                        self.screen.blit(self.plane_big_died4, (i.x, i.y))
                        self.screen.blit(self.plane_big_died5, (i.x, i.y))
                        self.screen.blit(self.plane_big_died6, (i.x, i.y))
                        self.big_enemy_group.remove(i)
                        score += 10
                        print("score:", score)
                        other.boom = True
                        self.count_bigplane_blood = 0
            for i in self.s_enemy_group:
                if (bullet.x >= i.x and bullet.x <= i.x + 69) and (bullet.y >= i.y and bullet.y <= i.y + 99):
                    self.count_splane_blood += 1
                    try:
                        self.bullet.remove(bullet)
                    except ValueError:
                        pass
                    if(self.count_splane_blood == 5):
                        self.screen.blit(self.plane_died_s1, (i.x, i.y))
                        self.screen.blit(self.plane_died_s2, (i.x, i.y))
                        self.screen.blit(self.plane_died_s3, (i.x, i.y))
                        self.screen.blit(self.plane_died_s4, (i.x, i.y))
                        self.s_enemy_group.remove(i)
                        score += 5
                        print("score:", score)
                        other.boom = True
                        self.count_splane_blood = 0
    def move(self):
        if self.up and self.y > 0:
            self.y -= 1
        if self.down and self.y < 600:
            self.y += 1
        if self.left and self.x > 0:
            self.x -= 1
        if self.right and self.x < 480-102:
            self.x += 1
    def fire(self):
        self.bullet.append(MeBullet(self.screen, self.x + 102 / 2 - 1, self.y, "images/bullet1.png"))



class MeBullet(BasePlane):
    def __init__(self, screen, x, y, image_filename):
        BasePlane.__init__(self, screen, x, y, image_filename)
    def move(self):
        self.y -= 1
    def out_of_rangebu(self):
        if self.y < 0:
            return True


class Enemy(BasePlane):
    def __init__(self, screen, x, y, image_filename):
        BasePlane.__init__(self, screen, x, y, image_filename)
        global enemy_group
        self.enemy_group = enemy_group
        self.boom = False
        self.bigboom = False
        self.bullets = []
        global big_enemy_group
        self.big_enemy_group = big_enemy_group
        global s_enemy_group
        self.s_enemy_group = s_enemy_group
    def display(self):
        if(len(self.enemy_group) < random.randint(0,5)):
            self.enemy_group.append(EnemyMove(self.screen, random.randint(0,420), random.randint(0,10), "images/enemy1.png"))
        if(random.randint(1,3000) == 1):   # 出现几率
            self.s_enemy_group.append(EnemyMove(self.screen, random.randint(0,420), random.randint(0,10), "images/enemy2.png"))
        if (random.randint(1, 10000) == 1):    # 出现几率
            self.big_enemy_group.append(EnemyMove(self.screen, random.randint(0, 390), random.randint(0, 10), "images/enemy3_n1.png"))
        for i in self.enemy_group:
            i.display()
            i.move()
            if i.out_of_range():
                self.enemy_group.remove(i)
            if self.boom:
                self.boom = False

        for i in self.s_enemy_group:
            i.display()
            i.move()
            if i.out_of_range():
                self.s_enemy_group.remove(i)
            if self.bigboom:
                self.boom = False
            else:
                for bullet in self.bullets:
                    bullet.display()
                    bullet.move()

        for i in self.big_enemy_group:
            i.display()
            i.move()
            if i.out_of_range():
                try:
                    self.enemy_group.remove(i)
                except ValueError:
                    pass
            if self.bigboom:
                self.boom = False

class EnemyBullet(BasePlane):
    def __init__(self, screen, x, y, image_filename):
        BasePlane.__init__(self, screen, x, y, image_filename)
    def move(self):
        self.y += 0.2
        if self.x <= me.x + 102 and self.x >= me.x and self.y <= me.y + 126 and self.y >= me.y:
            exit()

class EnemyMove(BasePlane):
    def __init__(self, screen, x, y, image_filename):
        BasePlane.__init__(self, screen, x, y, image_filename)
    def move(self):
        self.y += 0.1
        if random.randint(1, 20000) == 1:
            other.bullets.append(EnemyBullet(self.screen, self.x, self.y, "images/bullet2.png"))
        if self.x <= me.x + 102 and self.x >= me.x and self.y <= me.y + 126 and self.y >= me.y:
            exit()
    def out_of_range(self):
        if self.y > 700:
            return True



def check_key(plane):
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            key_press(event, plane)
        elif event.type == KEYUP:
            key_unpress(event, plane)
def key_press(event, plane):
    if event.key == K_UP:
        plane.up = True
    elif event.key == K_DOWN:
        plane.down = True
    elif event.key == K_RIGHT:
        plane.right = True
    elif event.key == K_LEFT:
        plane.left = True
    elif event.key == K_SPACE:
        plane.fire()



def key_unpress(event, plane):
    plane.up = False
    plane.down = False
    plane.left = False
    plane.right = False

def bg_move():
    global by1, by2
    by1 = by1 + 1
    by2 = by2 + 1
    if by1 >= 700:
        by1 = 0
    if by2 >= 0:
        by2 = -700
    screen.blit(bg_image1, (0, by1))
    screen.blit(bg_image2, (0, by2))


me = MyPlane(screen, x, y, "images/me1.png", "images/me2.png")
other = Enemy(screen, 0, 0, "images/enemy1.png")

while True:
    bg_move()
    me.display()
    me.move()
    check_key(me)
    other.display()
    pygame.display.update()
    FPSClock.tick(int(FPS))
    FPS += 0.01  # 控制运行速度 使游戏难度越来越高
