from pygame import *
from const import*
from game_sprite import GameSprite
from player import Player
# вынесем размер окна в константы для удобства
# W - width, ширина
# H - height, высота


# создание окна размером 700 на 500
window = display.set_mode((WIN_W, WIN_H))
# создание таймера
clock = time.Clock()
mixer.init()
mixer.music.load('src/undertale.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.5)

death = mixer.Sound('src/death.mp3')
hit = mixer.Sound('src/hit.mp3')
win = mixer.Sound('src/win.mp3')

font.init()
title_font = font.SysFont('comic sans', 70)
lost = title_font.render('Лошара', True, RED)
won = title_font.render('Молодец :)', True, GREEN)


# название окна
display.set_caption("Догонялки")

# задать картинку фона такого же размера, как размер окна
background = GameSprite("src/background.jpg", 0, 0,  (WIN_W, WIN_H))
hero = Player("src/hero.png", 50, 250,  (SIZE, SIZE))
cyborg = Player("src/cyborg.png", WIN_W-100, 250,  (SIZE, SIZE))
treasure = GameSprite("src/treasure.png", WIN_W-200, 100, (SIZE, SIZE))


# игровой цикл
game = True
finish = False
while game:
    if not finish:
        background.draw(window)
        hero.draw(window)
        cyborg.draw(window)
        treasure.draw(window)
        hero.update(K_w, K_s, K_a, K_d)
        cyborg.update(K_UP, K_DOWN, K_LEFT, K_RIGHT)

        if sprite.collide_rect(hero, cyborg):
            death.play()
            window.blit(lost, (250, 200))
            finish = True

        if sprite.collide_rect(hero,treasure):
            win.play()
            window.blit(won, (150, 200))
            finish = True


    # слушать события и обрабатывать
    for e in event.get():
        # выйти, если нажат "крестик"
        if e.type == QUIT:
            game = False
    # обновить экран, чтобы отобрзить все изменения
    display.update()
    clock.tick(FPS)