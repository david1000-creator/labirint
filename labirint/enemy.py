from pygame import*
from game_sprite import*
from random import choice


class Enemy(GameSprite):
    def __init__(self, img, x, y, size, speed=3):
        super().__init__(img, x, y, size)
        self.speedx = speed
        self.speedy = speed
        self.speed = speed

    # def update(self, collide, is_x=True, is_y=False):
    #     if not collide:
    #         self.rect.x += self.speedx
    #         self.rect.y += self.speedy
    #     else:
    #         # coef = choice((-1, 0))
    #         if is_x:
    #             self.speedx *= -1
    #         if is_y:
    #             self.speedy *= -1
    def update(self, start, end):
        if self.rect.x <= start or self.rect.x >= end:
            self.speed *= -1
        self.rect.x += self.speed