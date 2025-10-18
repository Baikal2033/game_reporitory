import pygame as pg

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
CIRCLE_WIDTH, CIRCLE_HIGHT = 150, 150
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
NIGHT_RED, NIGHT_GREEN, NIGHT_BLUE = (173, 76, 68), (68, 89, 60), (58, 88, 112)
MOON_GREY = (207, 215, 227)
GOLD_YELLOW = (173, 164, 106)
BROWN = (87, 50, 42)
GREY = (153, 147, 145)
flag = True
flag2 = True

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # экран
pg.display.set_caption("Игра")
clock = pg.time.Clock()

# слой №1 - статичный фон:
background = pg.Surface((WIN_WIDTH, WIN_HEIGHT))
# здесь нужен слой, так как мы не хотим перерисовывать по примитивам такой фон
background.fill(BROWN)
pg.draw.rect(background, GREY, (0, 100, WIN_WIDTH, 150))
pg.draw.rect(background, GREY, (0, WIN_HEIGHT - 250, WIN_WIDTH, 150))

circle_surf = pg.Surface((CIRCLE_WIDTH, CIRCLE_HIGHT), pg.SRCALPHA)
circle_surf.fill((0, 0, 0, 0))

circle_surf2 = pg.Surface((CIRCLE_WIDTH, CIRCLE_HIGHT), pg.SRCALPHA)
circle_surf2.fill((0, 0, 0, 0))

pg.draw.circle(circle_surf, (*GOLD_YELLOW, 190), (CIRCLE_WIDTH / 2, CIRCLE_HIGHT / 2), 40)

pg.draw.circle(circle_surf2, (*NIGHT_RED, 190), (CIRCLE_WIDTH / 2, CIRCLE_HIGHT / 2), 60)

circle_x = 0
circle_y = 100
step = 5

circle_x2 = 0
circle_y2 = 100
step2 = 3

screen.blit(background, (0, 0))
screen.blit(circle_surf, (circle_x, circle_y))
pg.display.update()  # обновляем окно, чтобы отобразить

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

    if flag == True:
        circle_y = 100
        circle_x += step

    if circle_x >= WIN_WIDTH:
        flag = False

    if circle_x <= -150:
        flag = True

    if flag == False:
        circle_y = WIN_HEIGHT - 250
        circle_x -= step


    if flag2 == True:
        circle_y2 = 100
        circle_x2 += step2

    if circle_x2 >= WIN_WIDTH:
        flag2 = False

    if circle_x2 <= -150:
        flag2 = True

    if flag2 == False:
        circle_y2 = WIN_HEIGHT - 250
        circle_x2 -= step2

    screen.blit(background, (0, 0))
    screen.blit(circle_surf, (circle_x, circle_y))
    screen.blit(circle_surf2, (circle_x2, circle_y2))
    pg.display.update()
