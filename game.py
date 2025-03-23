import pygame
from position import Position

pygame.init()

CUBE_SIZE = 25
CUBES_NUM = 20
WIDTH = CUBE_SIZE * CUBES_NUM
screen = pygame.display.set_mode((WIDTH, WIDTH))
WHITE  = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
screen.fill(WHITE)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
def draw_snake_part(pos):
    position = (pos.x * CUBE_SIZE,
                pos.y * CUBE_SIZE,
                CUBE_SIZE,
                CUBE_SIZE)
    pygame.draw.rect(screen, GREEN, position)

def draw_food(pos):
    radius = float(CUBE_SIZE) / 2
    position = (pos.x * CUBE_SIZE + radius,
                pos.y * CUBE_SIZE + radius)
    pygame.draw.circle(screen, BLUE, position,radius)

snake = [
    Position(2, 2),
    Position(3, 2),
    Position(4, 2),
    Position(5, 2),
    Position(5, 1),
]

def draw_snake(snake):
    for part in snake:
        draw_snake_part(part)
food = Position(11, 14)

def fill_bg():
    screen.fill(WHITE)

def draw(snake, food):
    fill_bg()
    draw_snake(snake)
    draw_food(food)
    pygame.display.update()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/