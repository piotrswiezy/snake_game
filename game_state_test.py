import unittest
from game_state import GameState
from position import Position
from direction import Direction

class GameStateTest(unittest.TestCase):

    def test_snake_should_move_right(self):
        state = GameState(
            snake = [
                Position(1, 2),
                Position(1, 3),
                Position(1, 4)
            ],
            direction = Direction.RIGHT,
            food = Position(10, 10),
            field_size = 20
        )

        state.step()

        expected_state = [
            Position(1, 3),
            Position(1, 4),
            Position(2, 4)
        ]
        self.assertEqual(expected_state, state.snake)

    def test_snake_should_move_left(self):
        state = GameState(
            snake = [
                Position(1, 2),
                Position(1, 3),
                Position(1, 4)
            ],
            direction = Direction.LEFT,
            food = Position(10, 10),
            field_size = 20
        )

        state.step()

        expected_state = [
            Position(1, 3),
            Position(1, 4),
            Position(0, 4)
        ]
        self.assertEqual(expected_state, state.snake)

    def test_snake_should_move_up(self):
        state = GameState(
            snake=[
                Position(1, 2),
                Position(2, 2),
                Position(3, 2)
            ],
            direction=Direction.UP,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(2, 2),
            Position(3, 2),
            Position(3, 1)
        ]
        self.assertEqual(expected_state, state.snake)

    def test_snake_should_move_down(self):
        state = GameState(
            snake=[
                Position(1, 1),
                Position(1, 2),
                Position(2, 2),
                Position(3, 2)
            ],
            direction=Direction.DOWN,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(1, 2),
            Position(2, 2),
            Position(3, 2),
            Position(3, 3)
        ]
        self.assertEqual(expected_state, state.snake)

    def test_snake_should_not_move_if_no_direction(self):
        state = GameState(
            snake=[
                Position(1, 1)
            ],
            direction=Direction.NO_DIRECTION,
            food=Position(10, 10),
            poisonous_food = Position(10, 20),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(1, 1)
        ]
        self.assertEqual(expected_state, state.snake)

    def test_snake_should_move_up_on_top(self):
        state = GameState(
            snake = [
                Position(2, 2),
                Position(2, 1),
                Position(2, 0)
            ],
            direction = Direction.UP,
            food = Position(10, 10),
            field_size = 20
        )

        state.step()

        expected_state = [
            Position(2, 1),
            Position(2, 0),
            Position(2, 19)
        ]
        self.assertEqual(expected_state, state.snake)

    def test_snake_should_move_right_on_edge(self):
        state = GameState(
            snake = [
                Position(17, 1),
                Position(18, 1),
                Position(19, 1)
            ],
            direction = Direction.RIGHT,
            food = Position(10, 10),
            field_size = 20
        )

        state.step()

        expected_state = [
            Position(18, 1),
            Position(19, 1),
            Position(0, 1)
        ]
        self.assertEqual(expected_state, state.snake)

    def test_snake_should_move_down_on_bottom(self):
        state = GameState(
            snake = [
                Position(1, 17),
                Position(1, 18),
                Position(1, 19)
            ],
            direction = Direction.DOWN,
            food = Position(10, 10),
            field_size = 20
        )

        state.step()

        expected_state = [
            Position(1, 18),
            Position(1, 19),
            Position(1, 0)
        ]
        self.assertEqual(expected_state, state.snake)

    def test_snake_should_move_left_on_edge(self):
        state = GameState(
            snake = [
                Position(2, 2),
                Position(1, 2),
                Position(0, 2)
            ],
            direction = Direction.LEFT,
            food = Position(10, 10),
            field_size = 20
        )

        state.step()

        expected_state = [
            Position(1, 2),
            Position(0, 2),
            Position(19, 2)
        ]
        self.assertEqual(expected_state, state.snake)

    def test_snake_eats_food(self):
        state = GameState(
            snake = [
                Position(1, 2),
                Position(2, 2),
                Position(3, 2)
            ],
            direction = Direction.UP,
            food = Position(3, 1),
            field_size = 20
        )

        state.step()

        expected_state = [
            Position(1, 2),
            Position(2, 2),
            Position(3, 2),
            Position(3, 1)
        ]
        self.assertEqual(expected_state, state.snake)

    def test_snake_dies(self):
        state = GameState(
            snake = [
                Position(1, 2),
                Position(2, 2),
                Position(3, 2),
                Position(3, 3),
                Position(2, 3)
            ],
            direction = Direction.UP,
            food = Position(3, 1),
            field_size = 25
        )

        state.step()
        self.assertTrue(state.dead)

        state.step()
        from game_state import INITIAL_SNAKE
        self.assertEqual(INITIAL_SNAKE, state.snake)
        self.assertFalse(state.food in state.snake)
        from game_state import INITIAL_DIRECTION
        self.assertEqual(INITIAL_DIRECTION, state.direction)
        self.assertEqual(25, state.field_size)
        self.assertEqual(False, state.food in state.snake)

    def test_snake_dies_after_eating_poison(self):
        state = GameState(
            snake=[
                Position(1, 2),
                Position(2, 2),
                Position(3, 2),
                Position(4, 2),
                Position(5, 2)
            ],
            direction=Direction.RIGHT,
            food=Position(3, 1),
            poisonous_food=Position(6, 2),
            field_size=25
        )

        state.step()
        self.assertTrue(state.dead)

        state.step()
        from game_state import INITIAL_SNAKE
        self.assertEqual(INITIAL_SNAKE, state.snake)
        self.assertFalse(state.poisonous_food in state.snake)
        from game_state import INITIAL_DIRECTION
        self.assertEqual(INITIAL_DIRECTION, state.direction)
        self.assertEqual(25, state.field_size)
        self.assertEqual(False, state.food in state.snake)

    def test_turn(self):
        state = GameState(
            snake = [
                Position(1, 2),
                Position(2, 2),
                Position(3, 2),
                Position(3, 3),
                Position(2, 3)
            ],
            direction = Direction.UP,
            food = Position(3, 1),
            field_size = 25
        )

        state.turn(Direction.LEFT)
        self.assertEqual(Direction.LEFT, state.direction)

        state.turn(Direction.UP)
        self.assertEqual(Direction.UP, state.direction)

        state.turn(Direction.DOWN)
        self.assertEqual(Direction.DOWN, state.direction)

        state.turn(Direction.RIGHT)
        self.assertEqual(Direction.DOWN, state.direction)

    def test_can_turn(self):
        state = GameState(
            snake = [
                Position(1, 2),
                Position(2, 2),
                Position(3, 2),
                Position(3, 3),
                Position(2, 3)
            ],
            direction = Direction.UP,
            food = Position(3, 1),
            field_size = 25
        )

        self.assertEqual(
            True,
            state.can_turn(Direction.LEFT)
        )

        self.assertEqual(
            True,
            state.can_turn(Direction.UP)
        )

        self.assertEqual(
            True,
            state.can_turn(Direction.DOWN)
        )

        self.assertEqual(
            False,
            state.can_turn(Direction.RIGHT)
        )