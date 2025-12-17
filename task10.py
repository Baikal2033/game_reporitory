import pygame as pg

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
GREEN_MINT = (225, 247, 228)

class Car:

    def __init__(self):
        self.speed = 3
        self.car_surf = pg.image.load('images\car.png')
        self.car_surf = self.car_surf.convert_alpha()
        self.rect = self.car_surf.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
        self.now_dr = 'up'

    def move(self, dx=0, dy=0):
        if (self.rect.left + dx * self.speed) > 0 and (self.rect.right + dx * self.speed) < WIN_WIDTH:
            self.rect.x += dx * self.speed
        if (self.rect.top + dy * self.speed) > 0 and (self.rect.bottom + dy * self.speed) < WIN_HEIGHT:
            self.rect.y += dy * self.speed

    def rotate(self, dr):
        if dr == 'left':
            if self.now_dr == 'up':
                new_surf = pg.transform.rotate(self.car_surf, 90)
                self.car_surf = new_surf
            if self.now_dr == 'down':
                new_surf = pg.transform.rotate(self.car_surf, -90)
                self.car_surf = new_surf
            if self.now_dr == 'right':
                new_surf = pg.transform.rotate(self.car_surf, -180)
                self.car_surf = new_surf
            self.now_dr = 'left'
        if dr == 'up':
            if self.now_dr == 'right':
                new_surf = pg.transform.rotate(self.car_surf, 90)
                self.car_surf = new_surf
            if self.now_dr == 'down':
                new_surf = pg.transform.rotate(self.car_surf, -180)
                self.car_surf = new_surf
            if self.now_dr == 'left':
                new_surf = pg.transform.rotate(self.car_surf, 90)
                self.car_surf = new_surf
            self.now_dr = 'up'
        if dr == 'right':
            if self.now_dr == 'left':
                new_surf = pg.transform.rotate(self.car_surf, -180)
                self.car_surf = new_surf
            if self.now_dr == 'down':
                new_surf = pg.transform.rotate(self.car_surf, 90)
                self.car_surf = new_surf
            if self.now_dr == 'up':
                new_surf = pg.transform.rotate(self.car_surf, -90)
                self.car_surf = new_surf
            self.now_dr = 'right'
        if dr == 'down':
            if self.now_dr == 'up':
                new_surf = pg.transform.rotate(self.car_surf, -180)
                self.car_surf = new_surf
            if self.now_dr == 'left':
                new_surf = pg.transform.rotate(self.car_surf, 90)
                self.car_surf = new_surf
            if self.now_dr == 'right':
                new_surf = pg.transform.rotate(self.car_surf, -90)
                self.car_surf = new_surf
            self.now_dr = 'down'



    def draw(self, screen):
        screen.blit(self.car_surf, self.rect)


pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Игра")
pg.display.set_icon(pg.image.load(r"images\icon.ico"))
clock = pg.time.Clock()

my_car = Car()

# отрисовка:
screen.fill(GREEN_MINT)
my_car.draw(screen)
# отрисовать машинку
pg.display.update()  # отображение отрисовки

# далее игровой цикл нужен, чтобы игра не завершилась, но у меня он не используется
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

    # двигаем машинку
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        my_car.rotate('left')
        my_car.move(dx=-1)
    if keys[pg.K_RIGHT]:
        my_car.rotate('right')
        my_car.move(dx=1)
    if keys[pg.K_UP]:
        my_car.rotate('up')
        my_car.move(dy=-1)
    if keys[pg.K_DOWN]:
        my_car.rotate('down')
        my_car.move(dy=1)


    # перерисовка ...
    screen.fill(GREEN_MINT)
    my_car.draw(screen)
    # отрисовать машинку
    pg.display.update()  # отображение перерисовки
