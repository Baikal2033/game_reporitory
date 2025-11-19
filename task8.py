import pygame as pg
import random

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
WHITE, BLACK, RED, AQUA = (244,244,169), (0, 0, 0), (255, 0, 0), (85,190,141)

class Balls:
    def __init__(self, pos):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = random.randint(10, 50)
        self.surf = pg.Surface((self.radius * 2, self.radius * 2), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=pos)
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*self.color, 255),
                       (self.rect.width / 2, self.rect.height / 2), self.radius)
        self.mask = pg.mask.from_surface(self.surf)
        self.alive = True

    def draw(self, screen):
        screen.blit(self.surf, self.rect)


class Player:
    SPEED = 3

    def __init__(self):
        self.width = 100
        self.height = 100
        self.surf = pg.Surface((self.width, self.height), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*AQUA, 255),
                       (self.rect.width / 2, self.rect.height / 2), 20)
        pg.draw.circle(self.surf, (*BLACK, 255),
                       (self.rect.width / 2, self.rect.height / 2), 20, 3)
        self.rad = 20
        self.mask = pg.mask.from_surface(self.surf)
        self.speed = Player.SPEED

    def move(self, dx=0, dy=0):
        if (self.rect.left + dx * self.speed) > 0 and (self.rect.right + dx * self.speed) < WIN_WIDTH:
            self.rect.x += dx * self.speed
        if (self.rect.top + dy * self.speed) > 0 and (self.rect.bottom + dy * self.speed) < WIN_HEIGHT:
            self.rect.y += dy * self.speed

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def explored(self, r):
        if self.rad + r / 5 < 50:
            self.rad += r / 5  # гарантируется что self.rad <= 50
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*AQUA, 255),
                       (self.rect.width / 2, self.rect.height / 2), self.rad)
        pg.draw.circle(self.surf, (*BLACK, 255),
                       (self.rect.width / 2, self.rect.height / 2), self.rad, 3)

def check_collusions(player, balls):
    for ball in balls:
        offset = (ball.rect.x - player.rect.x, ball.rect.y - player.rect.y)
        if player.mask.overlap(ball.mask, offset) is not None:
            if ball.alive == True:
                r = ball.radius
                ball.alive = False
                balls.append(Balls((random.randint(50, 950), random.randint(50, 550))))
                player.explored(r)



pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

balls = [Balls((random.randint(50, 950), random.randint(50, 550))), Balls((random.randint(50, 950), random.randint(50, 550))),
         Balls((random.randint(50, 950), random.randint(50, 550))), Balls((random.randint(50, 950), random.randint(50, 550)))]
player = Player()

screen.fill(WHITE)
for elem in balls:
    elem.draw(screen)
player.draw(screen)
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
    if keys[pg.K_LEFT]:
        player.move(dx=-1)
    if keys[pg.K_RIGHT]:
        player.move(dx=1)
    if keys[pg.K_UP]:
        player.move(dy=-1)
    if keys[pg.K_DOWN]:
        player.move(dy=1)

    check_collusions(player, balls)

    screen.fill(WHITE)
    for elem in balls:
        if elem.alive == True:
            elem.draw(screen)
    player.draw(screen)
    pg.display.update()
