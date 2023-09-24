import pygame
from Grid import Grid


pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
run = True

game_grid = Grid(10, 10, 100)
max_food_count = 10
tick_counter = 0

while run:
    screen.fill((100, 100, 100))
    for i in range(game_grid.get_grid_width()):
        for j in range(game_grid.get_grid_height()):
            node_type = game_grid.get_node(i,j).get_type()
            color = (25, 25, 25)
            if node_type == "food":
                color = (255, 0, 0)

            if node_type == "snake":
                color = (0, 255, 0)

            pygame.draw.rect(screen, color, pygame.Rect(i*50,j*50,49.9,49.9))

    if game_grid.food_count < max_food_count:
        game_grid.spawn_food()

    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        #game_grid.move_snake_right()
        game_grid.previous_move = "right"
    elif key[pygame.K_a]:
        #game_grid.move_snake_left()
        game_grid.previous_move = "left"
    elif key[pygame.K_w]:
        #game_grid.move_snake_up()
        game_grid.previous_move = "up"
    elif key[pygame.K_s]:
        #game_grid.move_snake_down()
        game_grid.previous_move = "down"

    if tick_counter >= 1:
        game_grid.repeat_move()
        tick_counter = 0

    tick_counter += 0.18

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
