from pygame import*


class Wall(sprite.Sprite):
    def __init__(self, color, x, y, w, h):
        super().__init__()
        self.color = color
        self.width = w
        self.height = h
        self.image = Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_wall(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))