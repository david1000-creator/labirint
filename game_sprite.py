from pygame import*


class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, size):
        super().__init__()
        self.image = transform.scale(
            image.load(img),
            # здесь - размеры картинки
            size
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def intersection(self, other):
        if self.rect.midtop[1] > other.rect.midtop[1]:
            return "top"
        elif self.rect.midleft[0] > other.rect.midleft[0]:
            return "left"
        elif self.rect.midright[0] < other.rect.midright[0]:
            return "right"
        else:
            return "bottom"
