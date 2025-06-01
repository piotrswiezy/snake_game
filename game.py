from math import sqrt

import pygame
from position import Position
from direction import Direction
from game_state import GameState, INITIAL_SNAKE, INITIAL_DIRECTION
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
clock = pygame.time.Clock()
paused = False
speed_up = False

def game_speed(speed):
    clock.tick(speed)

def draw_snake_part(pos, dead):
    position = (pos.x * CUBE_SIZE,
                pos.y * CUBE_SIZE,
                CUBE_SIZE,
                CUBE_SIZE)
    pygame.draw.rect(screen, RED if dead else GREEN, position)

def draw_food(pos, poisonous = False):
    food_color = BLUE if poisonous else RED
    radius = float(CUBE_SIZE) / 2
    position = (pos.x * CUBE_SIZE + radius,
                pos.y * CUBE_SIZE + radius)
    pygame.draw.circle(screen, food_color, position,radius)


def set_random_food_position():
    search = True
    while search:
        field_size = CUBES_NUM
        food = Position(
            randint(0, field_size - 1),
            randint(0, field_size - 1)
        )

def draw_snake(snake, dead):
    for part in snake:
        draw_snake_part(part, dead)

def fill_bg():
    screen.fill(BLACK)

def draw(snake, food, poison, dead):
    fill_bg()
    draw_snake(snake, dead)
    draw_food(food)
    draw_food(poison, True)
    pygame.display.update()

def set_initial_position():
        snake = INITIAL_SNAKE[:]
        direction = INITIAL_DIRECTION
        set_random_food_position()
state = GameState(snake=None, direction=None, food=None, poisonous_food=None, field_size=CUBES_NUM)
state.set_random_food_position()
state.set_initial_position()

while True:
    speed = 5 if not speed_up else 25
    game_speed(speed + sqrt(1 if state.dead else state.snake.__len__() // 2))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_ESCAPE:
                quit()
            if not paused:
                if event.key == pygame.K_LEFT:
                    state.turn(Direction.LEFT)

                elif event.key == pygame.K_RIGHT:
                    state.turn(Direction.RIGHT)

                elif event.key == pygame.K_UP:
                    state.turn(Direction.UP)

                elif event.key == pygame.K_DOWN:
                    state.turn(Direction.DOWN)

                elif event.key == pygame.K_BACKSPACE:
                    state.set_initial_position()

                elif event.key == pygame.K_LSHIFT:
                    speed_up = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                speed_up = False


    if not paused:
        draw(state.snake, state.food, state.poisonous_food, state.dead)
        state.step()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/