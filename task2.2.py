import pygame as pg

FPS = 60
WIN_WIDTH = 600
WIN_HEIGHT = 400
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
S = 2 # Скорость
flag = 'right'

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill(WHITE)  # белый фон
pg.display.set_caption("Игра")
clock = pg.time.Clock()

# до начала игрового цикла отображаем объекты:
r = 30  # радиус круга
# координаты центра круга:
x = 0  # скрываем за левой границей
y = WIN_HEIGHT / 4 + - 100 # выравниваем по центру по вертикали
width_ellipse = 80
pg.draw.ellipse(screen, ORANGE, (x, y, width_ellipse, 40))  # рисуем круг
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


    if x >= WIN_WIDTH - width_ellipse: #  Коснулся правой стенки
        flag = 'down'
        S += 1

    if y >= WIN_HEIGHT - 40 and flag == 'down':
        flag = 'left'
    if y >= WIN_HEIGHT - 50 and flag == 'down':
        S += 1

    if x <= 0  and flag == 'left':
        flag = 'up'
        y -= 2
    if x <= 10 and flag == 'left':
        S += 1

    if x <= 80 and y <= 5:
        flag = 'right'
        x += 2


    if flag == 'down':  # если еще нет
        y += S # то на следующей итерации цикла круг отобразится немного правее
    elif flag == 'right':  # если еще нет
        x += S
    elif flag == 'left':
        x -= S
    elif flag == 'up':
        y -= S

    screen.fill(WHITE)  # заливаем фон, стирая предыдущий круг
    pg.draw.ellipse(screen, ORANGE, (x, y, 80, 40)) # рисуем новый, сдвинутый круг

    pg.display.update()  # обновляем окно
