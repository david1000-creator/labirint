from pygame import*
from const import*
from game_sprite import GameSprite
class Player(GameSprite):
    def __init__ (self, img, x, y, size, speed = 3, hp = 3):
        super().__init__(img, x, y, size)
        self.speed = speed
        self.hp = hp
    def update(self, up, down,left, right):
        keys_pressed = key.get_pressed()
        if keys_pressed[up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[down] and self.rect.y < WIN_H - self.rect.height:
            self.rect.y += self.speed
        if keys_pressed[left] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[right] and self.rect.x < WIN_W - self.rect.width:
            self.rect.x += self.speed