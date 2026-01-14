import pygame as pg
import random

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
WHITE, BLACK, RED, AQUA, GREY = (255, 255, 255), (0, 0, 0), (255, 0, 0), (85,190,141), (110, 100, 99)

class Car(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r'images/car.png').convert_alpha()
        self.rect = self.image.get_rect(center=(500, 300))
        self.speed = 3

    def update(self, dx=0, dy=0):
        if (self.rect.left + dx * self.speed) > 0 and (self.rect.right + dx * self.speed) < WIN_WIDTH:
            self.rect.x += dx * self.speed
        if (self.rect.top + dy * self.speed) > 0 and (self.rect.bottom + dy * self.speed) < WIN_HEIGHT:
            self.rect.y += dy * self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class EnemyCar(pg.sprite.Sprite):
    def __init__(self):
        self.image_name = random.choice(['images/EnemyCar.png', 'images/EnemyCar2.png', 'images/EnemyCar3.png'])
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(self.image_name).convert_alpha()
        self.image = pg.transform.scale(self.image,
                                          (self.image.get_width() * 1.2,
                                           self.image.get_height() * 1.2))
        self.rect = self.image.get_rect(center=(random.randint(100, 900), 0))
        self.speed = random.randint(5, 9)

    def update(self):
        if self.rect.top < 1000:
            self.rect.y += self.speed
        else:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)


pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Игра")
pg.display.set_icon(pg.image.load(r"images\icon.ico"))
clock = pg.time.Clock()

background = pg.Surface((WIN_WIDTH, WIN_HEIGHT))
background.fill(GREY)
pg.draw.rect(background, WHITE, (WIN_WIDTH / 3 - 10, 0, 20, WIN_HEIGHT))
pg.draw.rect(background, WHITE, (WIN_WIDTH / 3 + WIN_WIDTH / 3 - 10, 0, 20, WIN_HEIGHT))

my_car = Car()
cnt = 0
dangerous_cars = pg.sprite.Group()

screen.blit(background, (0, 0))
my_car.draw(screen)
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

    cnt += 1
    if cnt == 60:
        dangerous_cars.add(EnemyCar())
        cnt = 0

    if pg.sprite.spritecollideany(my_car, dangerous_cars, collided=pg.sprite.collide_mask):
        flag_play = False
        break


    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        my_car.update(dx=-1)
    if keys[pg.K_RIGHT]:
        my_car.update(dx=1)
    if keys[pg.K_UP]:
        my_car.update(dy=-1)
    if keys[pg.K_DOWN]:
        my_car.update(dy=1)

    dangerous_cars.update()


    screen.blit(background, (0, 0))
    dangerous_cars.draw(screen)
    my_car.draw(screen)
    pg.display.update()
