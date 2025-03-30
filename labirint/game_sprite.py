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

    def intersection(self, sprite):
        left = max(self.rect.left, sprite.rect.left)
        width = min(self.rect.right, sprite.rect.right) - left
        top = max(self.rect.top, sprite.rect.top)
        height = min(self.rect.bottom, sprite.rect.bottom) - top
        return Rect(left, top, width, height)
