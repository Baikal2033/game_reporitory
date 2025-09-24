import pygame as pg

FPS = 60
WIN_WIDTH = 400
WIN_HEIGHT = 100
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
S = 0
D = False

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill(WHITE)  # белый фон
pg.display.set_caption("Игра")
clock = pg.time.Clock()

# до начала игрового цикла отображаем объекты:
r = 30  # радиус круга
# координаты центра круга:
x = 0  # скрываем за левой границей
y = WIN_HEIGHT / 4 # выравниваем по центру по вертикали
pg.draw.rect(screen, ORANGE, (x, y, 40, 40))  # рисуем круг
pg.display.update()  # обновляем окно

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

    # изменение состояний объектов:
    # если круг полностью скрылся за правой границей
    if x >= WIN_WIDTH - 40:
        x -= (2 + S)
        D = True
        S += 1

    if x <= 0:
        x += (2 + S)
        D = False
        S += 1

    elif D == True:  # если еще нет
        x -= (2 + S)  # то на следующей итерации цикла круг отобразится немного правее
    elif D == False:  # если еще нет
        x += (2 + S)

    screen.fill(WHITE)  # заливаем фон, стирая предыдущий круг
    pg.draw.rect(screen, ORANGE, (x, y, 40, 40)) # рисуем новый, сдвинутый круг

    pg.display.update()  # обновляем окно
