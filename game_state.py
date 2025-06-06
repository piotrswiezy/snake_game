from position import Position
from direction import Direction
from random import randint

INITIAL_SNAKE = [Position(1, 2)]
INITIAL_DIRECTION = Direction.NO_DIRECTION
NONE = []

class GameState:
    def __init__(self,
                 snake = None,
                 direction = INITIAL_DIRECTION,
                 food = None,
                 poisonous_food = None,
                 field_size = 20):

        if snake is None:
            snake = INITIAL_SNAKE[:]
        self.snake = snake
        self.direction = direction
        self.field_size = field_size
        self.speed_up = False
        self.points = 0
        self.dead = False
        self.success = False
        self.game_ower = False
        self.hearts = 5

        if food is None:
            self.set_random_food_position()
        else:
            self.food = food

        if poisonous_food is None:
            self.set_random_food_position(True)
        else:
            self.poisonous_food = poisonous_food

    def set_initial_position(self):
        self.snake = INITIAL_SNAKE[:]
        self.direction = INITIAL_DIRECTION
        self.set_random_food_position()
        self.set_random_food_position(True)
        self.points = 0
        self.dead = False
        self.success = False
        self.game_ower = False

    def next_head(self, direction):
        pos = self.snake[-1]
        if direction == Direction.UP:
            return Position(
                pos.x,
                (pos.y - 1) % self.field_size
            )
        elif direction == Direction.DOWN:
            return Position(
                pos.x,
                (pos.y + 1) % self.field_size
            )
        elif direction == Direction.RIGHT:
            return Position(
                (pos.x + 1) % self.field_size,
                pos.y
            )
        elif direction == Direction.LEFT:
            return Position(
                (pos.x - 1) % self.field_size,
                pos.y
            )
        raise Exception(f"{direction} - not known direction")

    def set_random_food_position(self, poisonous = False):
        search = True
        while search:
            if poisonous:
                self.poisonous_food = [Position(
                    randint(0, self.field_size - 1),
                    randint(0, self.field_size - 1)
                )]
                search = self.poisonous_food in self.snake
            else:
                self.food = [Position(
                    randint(0, self.field_size - 1),
                    randint(0, self.field_size - 1)
                )]
                search = self.food in self.snake



    def can_turn(self, direction):
        new_head = self.next_head(direction)
        if self.snake.__len__() > 1:
            return new_head != self.snake[-2]
        return True

    def step(self):
        if self.dead:
            self.set_initial_position()
            self.hearts -= 1
            return
        if self.success or self.game_ower:
            self.food = NONE
            self.poisonous_food = NONE
            self.snake = NONE
        if self.points == 40:
            self.success = True

        elif self.hearts == 0:
            self.game_ower = True

        if self.direction == Direction.NO_DIRECTION:
            return

        new_head = self.next_head(self.direction)

        collision = new_head in self.snake or new_head in self.snake
        if collision:
            self.dead = True
            return

        self.snake.append(new_head)

        if new_head == self.food:
            self.set_random_food_position()
            self.points += 1
            print(f"Masz {self.points} punktów")
        elif new_head == self.poisonous_food:
            self.set_random_food_position(True)
            self.points -= 1
            if self.points < 0:
                self.dead = True
                return
            print(f"Masz {self.points} punktów")
        else:
            self.snake = self.snake[1:]

    def turn(self, direction):
        if self.can_turn(direction):
            self.direction = direction
