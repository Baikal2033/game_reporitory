import random
import pygame as pg

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
BROWN = (87, 50, 42)
GREY = (153, 147, 145)

class Ball:
    SIZE = WIN_HEIGHT * 1 / 4

    def __init__(self):
        self.move_speed = random.randint(2, 7)
        rd_color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        rd_radius = random.randint(20, 50)
        self.surf = pg.Surface((Ball.SIZE, Ball.SIZE), pg.SRCALPHA)
        self.rect = self.surf.get_rect(topleft=(0, 100))
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*rd_color, 50), (self.rect.width / 2, self.rect.width / 2), rd_radius)
        self.rect_top = self.rect.top

    def draw(self, screen):  # отрисовка снаряда на экране слоем self.surf
        screen.blit(self.surf, self.rect)

    def move(self):
        # if на первой трубе:
        #     if можем ->:
        #         ->
        #     else:
        #         переход на 2-ую трубу
        # else:
        #     if можем <-:
        #         <-
        #     else:
        #         переход на 1-ую трубу
        if self.rect.top == self.rect_top:
            if self.rect.left < WIN_WIDTH:
                self.rect.right += self.move_speed
            else:
                self.rect.top += 250
        else:
            if self.rect.right > self.move_speed:
                self.rect.left -= self.move_speed
            else:
                self.rect.top -= 250



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

ball_list = [Ball(), Ball()]

screen.blit(background, (0, 0))
for elem in ball_list:
    elem.draw(screen)
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

    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        ball_list.append(Ball())

    for elem in ball_list:
        elem.move()

    screen.blit(background, (0, 0))
    for elem in ball_list:
        elem.draw(screen)
    pg.display.update()
