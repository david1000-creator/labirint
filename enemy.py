from pygame import*
from game_sprite import*
from random import randint, choice
from const import WIN_H, WIN_W


class Enemy(GameSprite):
    def __init__(self, img, x, y, size, speed=2):
        super().__init__(img, x, y, size)
        self.speedx = speed * randint(-1, 1)
        self.speedy = speed * randint(-1, 1)
        self.speed = speed
        self.count_zeros = 0
    
    def forward(self):
        if self.rect.y <= 0 or self.rect.y >= WIN_H - self.rect.height:
            self.speedy *= -1
        if self.rect.x <= 0 or self.rect.x >= WIN_W - self.rect.width:
            self.speedx *= -1
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def update_pos(self, other):
        
        side = self.intersection(other)
        print(side)
        add_vector = randint(-1, 1)
        if side in ['left', 'right']:
            self.speedx *= -1
            self.speedy *= add_vector
            self.forward()
        if side in ['top', 'bottom']:
            self.speedy *= -1
            self.speedx *= add_vector
            self.forward()
        if self.speedx == 0 or self.speedy == 0:
            self.count_zeros += 1
        if self.count_zeros > 5:
            if self.speedx == 0:
                self.speedx = choice([-1, 1])
            else:
                self.speedy = choice([-1, 1])
        if self.speedx == 0 and self.speedy == 0:
            self.speedx = choice([-1, 1])
            self.speedy = choice([-1, 1])
    def update(self, start, end):
        if self.rect.x <= start or self.rect.x >= end:
            self.speed *= -1
        self.rect.x += self.speed