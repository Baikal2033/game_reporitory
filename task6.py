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

circle_surf1 = pg.Surface((CIRCLE_WIDTH, CIRCLE_HIGHT), pg.SRCALPHA)
rect1 = circle_surf1.get_rect(topleft=(0, 100))
circle_surf1.fill((0, 0, 0, 0))
pg.draw.circle(circle_surf1, (*GOLD_YELLOW, 190), (rect1.width / 2, rect1.width / 2), 40)

circle_surf2 = pg.Surface((CIRCLE_WIDTH, CIRCLE_HIGHT), pg.SRCALPHA)
rect2 = circle_surf2.get_rect(topleft=(0, 100))
circle_surf2.fill((0, 0, 0, 0))

pg.draw.circle(circle_surf2, (*NIGHT_RED, 190), (rect2.width / 2, rect2.width / 2), 60)

step1 = 5
step2 = 3

screen.blit(background, (0, 0))
screen.blit(circle_surf1, rect1)
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
        rect1.right += step1

    if rect1.left >= WIN_WIDTH:
        flag = False
        rect1.y = WIN_HEIGHT - 250

    if rect1.right <= 0:
        flag = True
        rect1.y = 100

    if flag == False:
        rect1.left -= step1



    if flag2 == True:
        rect2.right += step2

    if rect2.left >= WIN_WIDTH:
        flag2 = False
        rect2.y = WIN_HEIGHT - 250

    if rect2.right <= 0:
        flag2 = True
        rect2.y = 100

    if flag2 == False:
        rect2.left -= step2

    screen.blit(background, (0, 0))
    screen.blit(circle_surf1, rect1)
    screen.blit(circle_surf2, rect2)
    pg.display.update()
