import random

import pygame as pg

FPS = 60
WIDTH, HEIGHT = 600, 500
MINT = (230, 254, 212)
ORANGE = (255, 150, 100)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

# до начала игрового цикла отображаем объекты:
# координаты центра круга
x, y = WIDTH / 2, HEIGHT / 2  # координаты центра круга
r = 30  # радиус круга
pg.draw.circle(screen, ORANGE, (x, y), r)  # рисуем круг
pg.display.update()  # обновляем окно
rd = ORANGE

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                screen.fill(MINT)  # заливаем фон, стирая предыдущий круг
                rd = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                pg.draw.circle(screen, rd, (x, y), r)  # рисуем новый, сдвинутый круг

    if not flag_play:
        break

    # изменение состояний объектов:
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and x >= 0 + r:
        x -= 3
    if keys[pg.K_RIGHT] and x <= WIDTH - r:
        x += 3
    if keys[pg.K_UP] and y >= 0 + r:
        y -= 3
    if keys[pg.K_DOWN] and y <= HEIGHT - r:
        y += 3


# Проверяем доходит ли круг до конца экрана

    screen.fill(MINT)  # заливаем фон, стирая предыдущий круг
    pg.draw.circle(screen, rd, (x, y), r)  # рисуем новый, сдвинутый круг

    pg.display.update()  # обновляем окно
