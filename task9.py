import pygame as pg
import random

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
WHITE, BLACK, RED, AQUA, BIRUZ, GREY = (244,244,169), (0, 0, 0), (255, 0, 0), (85,190,141), (48,213,200), (67,73,81)

class Text:
    def __init__(self, text, text_size, text_color, text_pos):
        self.font = pg.font.SysFont(None, text_size)
        self.suft = self.font.render(text, True, text_color)
        self.rect = self.suft.get_rect(center=text_pos)

    def draw(self, screen):
        screen.blit(self.suft, self.rect)

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
    def explore(self):
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
player = Player()

class Button:
    def __init__(self, text, text_size, text_color, button_color, button_pos):
        self.font = pg.font.SysFont(None, text_size)
        self.text_surf = self.font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=button_pos)
        self.button_surf = pg.Surface((self.text_surf.get_width() + 50, self.text_surf.get_height() + 50))
        self.button_rect = self.button_surf.get_rect(center=button_pos)
        self.button_surf.fill(button_color)
        pg.draw.rect(self.button_surf, BLACK, (0, 0, self.button_rect.width, self.button_rect.height), 3)

    def draw(self, screen):
        screen.blit(self.button_surf, self.button_rect)
        screen.blit(self.text_surf, self.text_rect)


def check_click_on_button(button):
    if button.button_rect.collidepoint(pg.mouse.get_pos()):
        print("𝑩𝒖𝒕𝒕𝒐𝒏 𝒘𝒂𝒔 𝒑𝒓𝒆𝒔𝒔𝒆𝒅")
        player.rad = 20
        player.explore()

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

balls = [Balls((random.randint(50, 950), random.randint(50, 550))), Balls((random.randint(50, 950), random.randint(50, 550))),
         Balls((random.randint(50, 950), random.randint(50, 550))), Balls((random.randint(50, 950), random.randint(50, 550)))]

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
        my_text = Text(f"Размер: {player.rad}", 32, GREY, (WIN_WIDTH / 2, WIN_HEIGHT * 1 / 3 - 150))
        my_button = Button("Сброс", 64, BLACK, BIRUZ, (WIN_WIDTH / 2, WIN_HEIGHT * 2 / 3 + 100))
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if check_click_on_button(my_button):
                print("𝑩𝒖𝒕𝒕𝒐𝒏 𝒘𝒂𝒔 𝒑𝒓𝒆𝒔𝒔𝒆𝒅")
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
    my_button.draw(screen)
    for elem in balls:
        if elem.alive == True:
            elem.draw(screen)
    player.draw(screen)
    my_text.draw(screen)
    pg.display.update()
