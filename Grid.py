import random

from Node import Node


class Grid:

    def __init__(self, width, height, node_size):
        self.width = width
        self.height = height
        self.node_size = node_size
        self.grid = self.create_grid()
        self.snake = self.create_snake()
        self.food_count = 0
        self.previous_move = "right"
        self.check_move = "right"

    def create_grid(self):
        columns = []
        for i in range(self.width):
            column = []
            for j in range(self.height):
                column.append(Node(self.node_size, i, j))
            columns.append(column)
        return columns

    def create_snake(self):
        head_node_x = int(self.width/2)
        head_node_y = int(self.height/2)
        body_node_x = head_node_x - 1
        body_node_y = head_node_y

        body_node_x2 = body_node_x - 1

        head_node = self.get_node(head_node_x, head_node_y)
        body_node = self.get_node(body_node_x, body_node_y)
        body_node2 = self.get_node(body_node_x2, body_node_y)
        head_node.set_type("snake")
        body_node.set_type("snake")
        body_node2.set_type("snake")
        return [head_node, body_node, body_node2]

    def move_snake_right(self):
        ate = False
        next_x = self.snake[0].x + 1
        next_y = self.snake[0].y

        if next_x < self.width and next_y < self.height:
            ate = self.check_for_food_and_collison(next_x, next_y)
            previous_x = next_x
            previous_y = next_y
            for i in range(len(self.snake)):
                snake_part = self.snake[i]
                self.set_node(previous_x, previous_y, "snake")
                self.snake[i] = self.get_node(previous_x, previous_y)
                snake_part.set_type("empty")
                previous_x = snake_part.x
                previous_y = snake_part.y

            if ate:
                self.set_node(previous_x, previous_y, "snake")
                self.snake.append(self.get_node(previous_x, previous_y))

    def move_snake_left(self):
        ate = False
        next_x = self.snake[0].x - 1
        next_y = self.snake[0].y

        if next_x < self.width and next_y < self.height:
            ate = self.check_for_food_and_collison(next_x, next_y)
            previous_x = next_x
            previous_y = next_y
            for i in range(len(self.snake)):
                snake_part = self.snake[i]
                self.set_node(previous_x, previous_y, "snake")
                self.snake[i] = self.get_node(previous_x, previous_y)
                snake_part.set_type("empty")
                previous_x = snake_part.x
                previous_y = snake_part.y

            if ate:
                self.set_node(previous_x, previous_y, "snake")
                self.snake.append(self.get_node(previous_x, previous_y))

    def move_snake_up(self):
        ate = False
        next_x = self.snake[0].x
        next_y = self.snake[0].y - 1
        if next_x < self.width and next_y < self.height:
            ate = self.check_for_food_and_collison(next_x, next_y)
            previous_x = next_x
            previous_y = next_y
            for i in range(len(self.snake)):
                snake_part = self.snake[i]
                self.set_node(previous_x, previous_y, "snake")
                self.snake[i] = self.get_node(previous_x, previous_y)
                snake_part.set_type("empty")
                previous_x = snake_part.x
                previous_y = snake_part.y

            if ate:
                self.set_node(previous_x, previous_y, "snake")
                self.snake.append(self.get_node(previous_x, previous_y))

    def move_snake_down(self):
        ate = False
        next_x = self.snake[0].x
        next_y = self.snake[0].y + 1
        if next_x < self.width and next_y < self.height:
            ate = self.check_for_food_and_collison(next_x, next_y)
            previous_x = next_x
            previous_y = next_y
            for i in range(len(self.snake)):
                snake_part = self.snake[i]
                self.set_node(previous_x, previous_y, "snake")
                self.snake[i] = self.get_node(previous_x, previous_y)
                snake_part.set_type("empty")
                previous_x = snake_part.x
                previous_y = snake_part.y

            if ate:
                self.set_node(previous_x, previous_y, "snake")
                self.snake.append(self.get_node(previous_x, previous_y))

    def get_node(self, pos_x, pos_y):
        node_column = self.grid[pos_x]
        node = node_column[pos_y]
        return node

    def set_node(self, pos_x, pos_y, node_type):
        node = self.get_node(pos_x, pos_y)
        node.set_type(node_type)

    def get_grid_width(self):
        return self.width

    def get_grid_height(self):
        return self.height

    def spawn_food(self):
        looking_for_spawn = True
        while looking_for_spawn:
            y = random.randint(0, self.height - 1)
            x = random.randint(0, self.width - 1)
            node = self.get_node(x, y)
            if node.type == "empty":
                looking_for_spawn = False
                self.set_node(x, y, "food")
                self.food_count += 1

    def repeat_move(self):
        if self.previous_move == "right" and self.check_move != "left":
            self.move_snake_right()
            self.check_move = "right"
        elif self.previous_move == "left" and self.check_move != "right":
            self.move_snake_left()
            self.check_move = "left"
        elif self.previous_move == "up" and self.check_move != "down":
            self.move_snake_up()
            self.check_move = "up"
        elif self.previous_move == "down" and self.check_move != "up":
            self.move_snake_down()
            self.check_move = "down"

    def check_for_food_and_collison(self, next_head_x, next_head_y):
        if next_head_x == self.width:
            print("endgame")
            self.snake = []
        if next_head_y == self.height:
            print("endgame")
            self.snake = []

        next_node = self.get_node(next_head_x, next_head_y)
        if next_node.type == "snake":
            print("killedurself")
            return False
        elif next_node.type == "food":
            print("ate")
            self.food_count -= 1
            return True








