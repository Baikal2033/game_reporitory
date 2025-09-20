import pygame as pg

FPS = 60
WIDTH, HEIGHT = 1000, 600

# цвета выбраны с сайта: https://htmlcolorcodes.com/
BLUE = (8, 28, 194)
MINT = (29, 204, 160)
BLACK = (0, 0, 0)
ORANGE = (204, 134, 29)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLUE)  # заливка фона
pg.display.set_caption("Дом")
clock = pg.time.Clock()

# Квадрат
pg.draw.rect(screen, MINT, (300, 150, 300, 300))
pg.draw.rect(screen, BLACK, (300, 150, 300, 300), 8)
# Круг
pg.draw.circle(screen, BLACK, [WIDTH / 2 - 50, HEIGHT / 2], 50, 8)
# Крыша
pg.draw.polygon(screen, MINT,
                  [[300, 150], [WIDTH / 2 - 50, 40], [600, 150]])
pg.draw.lines(screen, BLACK, True,
                  [[300, 150], [WIDTH / 2 - 50, 40], [600, 150]], 8)
# Солнце
pg.draw.circle(screen, ORANGE, (90, 90), 80)

# отображаем нарисованные объекты
pg.display.update()

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    pg.display.update()
