import pygame
from position import Position
from direction import Direction
from game_state import GameState
from random import randint

pygame.init()

CUBE_SIZE = 25
CUBES_NUM = 40
WIDTH = CUBE_SIZE * CUBES_NUM
screen = pygame.display.set_mode((WIDTH, WIDTH))
WHITE  = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
screen.fill(WHITE)
pygame.display.update()



def draw_snake_part(pos):
    position = (pos.x * CUBE_SIZE,
                pos.y * CUBE_SIZE,
                CUBE_SIZE,
                CUBE_SIZE)
    pygame.draw.rect(screen, GREEN, position)

def draw_food(pos):
    food_color = RED
    radius = float(CUBE_SIZE) / 2
    position = (pos.x * CUBE_SIZE + radius,
                pos.y * CUBE_SIZE + radius)
    pygame.draw.circle(screen, food_color, position,radius)

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
    screen.fill(BLACK)

def draw(snake, food):
    fill_bg()
    draw_snake(snake)
    draw_food(food)
    pygame.display.update()

state = GameState(
    None, None, None, CUBES_NUM
)
state.set_initial_position()

clock = pygame.time.Clock()
while True:
    clock.tick(5 + state.snake.__len__() // 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                state.turn(Direction.LEFT)

            elif event.key == pygame.K_RIGHT:
                state.turn(Direction.RIGHT)

            elif event.key == pygame.K_UP:
                state.turn(Direction.UP)

            elif event.key == pygame.K_DOWN:
                state.turn(Direction.DOWN)
    state.step()
    draw(state.snake, state.food)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/