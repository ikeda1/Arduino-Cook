"""
Nome: Pedro Henrique Ikeda
TIA: 32016344

Nome: Luiz Szajnbok
TIA: 32086083
"""

import pygame as pg
import random
from media import *

class Player(object):
    def __init__(self, x, y, vel=7, width=32, height=40):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walk_count = 0
        self.load_images()
        self.hitbox = (self.x, self.y, 32, 40)
        self.score()
        self.life()
        
    
    def update(self, screen):
        if self.walk_count + 1 >= 9:
            self.walk_count = 0

        if self.left or (self.up and self.left):
            screen.blit(self.walk_l[self.walk_count//3], (self.x, self.y))
            self.image = self.walk_l[self.walk_count//3]
            self.walk_count += 1
        elif self.right or (self.up and self.left):
            screen.blit(self.walk_r[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1
        elif self.up:
            screen.blit(self.walk_u[self.walk_count//3], (self.x, self.y))
            self.rect = (self.x, self.y, 32, 40)
            self.walk_count += 1
        elif self.down:
            screen.blit(self.walk_d[self.walk_count//3], (self.x, self.y))
            self.rect = (self.x, self.y, 32, 40)
            self.walk_count += 1
        else:
            screen.blit(self.char, (self.x, self.y))
            # self.rect = char[0].get_rect()
        self.score_text = self.font.render(f"Pontuação: {self.score_cont}", True, BLACK)
        self.life_text = self.font.render(f"Vidas: {self.life_cont} x", True, BLACK)
        screen.blit(self.life_text, [400, 10])
        screen.blit(self.score_text, [24, 10])
        self.hitbox = (self.x, self.y, 32, 40)
        # pg.draw.rect(screen, (255,0,0), self.hitbox,2)

    def score(self):
        self.score_cont = 0
        self.font = pg.font.SysFont("Segoe UI Black", 20)
    
    def life(self):
        self.life_cont = 5

    def load_images(self):
        self.char = pg.image.load("img\\game\\player\\d_01.png")
        self.walk_l = [pg.image.load("img\\game\\player\\l_01.png"), pg.image.load("img\\game\\player\\l_02.png"), pg.image.load("img\\game\\player\\l_03.png")]
        self.walk_r = [pg.image.load("img\\game\\player\\r_01.png"), pg.image.load("img\\game\\player\\r_02.png"), pg.image.load("img\\game\\player\\r_03.png")]
        self.walk_d = [pg.image.load("img\\game\\player\\d_01.png"), pg.image.load("img\\game\\player\\d_02.png"), pg.image.load("img\\game\\player\\d_03.png")]
        self.walk_u = [pg.image.load("img\\game\\player\\u_01.png"), pg.image.load("img\\game\\player\\u_02.png"), pg.image.load("img\\game\\player\\u_03.png")]
        self.hearts = hearts

    def hit(self):
        self.life_cont -= 1
        # print("HIT")
    
    def get_item(self):
        self.score_cont += 10
        item_snd.play()
        # print("ITEM")

class Item(object):
    def __init__(self, width=25, height=25):
        self.load_images()
        self.x = random.randrange(50, 620)
        self.y = random.randrange(50, 350)
        self.image = self.itens[random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])]
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)

    def load_images(self):
        self.maca = pg.image.load("img\\game\\itens\\01.png")
        self.maca = pg.transform.scale(self.maca, [25, 25])
        self.pizza = pg.image.load("img\\game\\itens\\02.png")
        self.pizza = pg.transform.scale(self.pizza, [25, 25])
        self.frango = pg.image.load("img\\game\\itens\\03.png")
        self.frango = pg.transform.scale(self.frango, [25, 25])
        self.cookie = pg.image.load("img\\game\\itens\\04.png")
        self.cookie = pg.transform.scale(self.cookie, [25, 25])
        self.donut = pg.image.load("img\\game\\itens\\05.png")
        self.donut = pg.transform.scale(self.donut, [25, 25])
        self.hamb = pg.image.load("img\\game\\itens\\06.png")
        self.hamb = pg.transform.scale(self.hamb, [25, 25])
        self.sushi = pg.image.load("img\\game\\itens\\07.png")
        self.sushi = pg.transform.scale(self.sushi, [25, 25])
        self.ccake = pg.image.load("img\\game\\itens\\08.png")
        self.ccake = pg.transform.scale(self.ccake, [25, 25])
        self.bum = pg.image.load("img\\game\\itens\\09.png")
        self.bum = pg.transform.scale(self.bum, [25, 25])
        self.itens = [self.maca, self.pizza, self.frango, self.cookie, self.hamb, self.donut, self.sushi, self.ccake, self.bum]

    def update(self, screen):
        # self.hitbox = (self.x, self.y, self.width, self.height)
        # pg.draw.rect(screen, (255,0,0), (self.rect),2)
        screen.blit(self.image, (self.x, self.y))

class Projectile(object):
    def __init__(self, width=22, height=22):
        self.x = random.choice([15, 648])
        self.y = random.choice([50, 100, 150, 200, 250, 300, 330])
        self.init_x = self.x
        self.init_y = self.y
        self.side = True
        self.rand = random.randint(1, 2)
        self.width = width
        self.height = height
        self.walk_count = 0
        self.enemy_count = 0
        self.dx = random.randrange(6, 12, 3)
        if self.x > 600:
            self.dx *= -1
            self.side = False
            self.init_x = self.x - 24
        self.load_images()
        # self.dy = random.randrange(-10, 10)
        self.hitbox = (self.x, self.y, self.width, self.height)
    
    def update(self, screen):
        if self.walk_count + 1 >= 12:
            self.walk_count = 0

        if self.side and self.enemy_count < 25:
            screen.blit(self.enemy[1], (self.init_x, self.init_y))
        elif not self.side and self.enemy_count < 25:
            screen.blit(self.enemy[0], (self.init_x, self.init_y))

        # self.rect.topleft = (self.x, self.y)
        self.hitbox = (self.x, self.y, self.width, self.height)
        # pg.draw.rect(screen, (255,0,0), (self.hitbox),2)
        if self.rand == 1:
            screen.blit(self.bottle[self.walk_count//3], (self.x, self.y))
        elif self.rand == 2:
            screen.blit(self.spoon[self.walk_count//3], (self.x, self.y))
        self.enemy_count += 1
        self.walk_count += 1

    def hit(self):
        if self.rand == 1:
            hit_snd[1].play()
        elif self.rand == 2:
            hit_snd[0].play()

    def load_images(self):
        self.enemy = [enemy_left, enemy_right]
        self.spoon = spoon
        self.bottle = bottle