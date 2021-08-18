import pygame
import random
import time
import numpy as np
#globals

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
block_size = 25
height = 800
width = 500
columns = 10
rows = 15


def create_grid(current_positions):
    grid = [[0 for i in range(columns)] for j in range(rows)]
    for i in range(columns):
        for j in range(rows):
            if current_positions[j][i] == 1:
                grid[j][i] = 1
            else:
                grid[j][i] = 0
    return grid


def check_loser(current_positions):
    for i in range(columns):
        if current_positions[i][rows] == 1:
            return True
        else:
            return False


def create_shape(shape, current_positions):
    if shape == "T":
        current_positions[0][4] = 1
        current_positions[0][3] = 1
        current_positions[0][5] = 1
        current_positions[1][4] = 1
        current_positions[2][4] = 1
    if shape == "J":
        current_positions[0][4] = 1
        current_positions[1][4] = 1
        current_positions[2][4] = 1
        current_positions[2][3] = 1
        #current_positions[12][7] = 1
    if shape == "O":
        current_positions[0][4] = 1
        current_positions[0][5] = 1
        current_positions[1][4] = 1
        current_positions[1][5] = 1
    if shape == "P":
        current_positions[0][4] = 1
        current_positions[0][3] = 1
        current_positions[1][3] = 1
        current_positions[2][3] = 1
    if shape == "L":
        current_positions[0][4] = 1
        current_positions[1][4] = 1
        current_positions[2][4] = 1
        current_positions[2][5] = 1
    return current_positions


def shift_down(current_positions):
    #current_positions = np.roll(current_positions, 1, axis=0)
    for i in range(columns):
        for j in range(rows-1, -1, -1):
            if (current_positions[j][i] == 1) and j != (rows-1) and not hit_bottom(current_positions):          #and (current_positions[j+1][i] != 2)
                current_positions[j][i] = 0
                current_positions[j+1][i] = 1
            #print(j)

    return current_positions


def draw_shape(grid):
    #global screen
    for i in range(columns):
        for j in range(rows):
            color = WHITE
            if grid[j][i] == 2:
                color = RED
            if grid[j][i] == 1:
                color = GREEN
            pygame.draw.rect(screen, color, [(5 + block_size) * i + 5, (5 + block_size) * j + 5, block_size, block_size])

    clock.tick(60)
    pygame.display.flip()
    #return screen


def create_bottom(current_positions):
    for i in range(columns):
        for j in range(rows-1, -1, -1):
            if current_positions[j][i] == 1 and j == rows-1:
                current_positions[j][i] = 2
                current_positions = convert(current_positions)
            if j != (rows-1) and current_positions[j][i] == 1 and current_positions[j+1][i] == 2:
                current_positions[j][i] = 2
                current_positions = convert(current_positions)
            #print(j)
    return current_positions


def convert(current_positions):
    for i in range(columns):
        for j in range(rows-1):
            if current_positions[j][i] == 1:
                current_positions[j][i] = 2
    return current_positions


def shift_right(current_positions):
    for i in range(columns-1, 0, -1):
        for j in range(rows-1):
            if current_positions[j][i] == 1 and i != columns-1:
                current_positions[j][i] = 0
                current_positions[j][i+1] = 1
    return current_positions


def shift_left(current_positions):
    for i in range(columns):
        for j in range(rows-1):
            if current_positions[j][i] == 1 and i != 0:
                current_positions[j][i] = 0
                current_positions[j][i-1] = 1
    return current_positions



def hit_bottom(current_positions):
    #hit = False
    for i in range(columns):
        for j in range(rows):
            if current_positions[j][i] == 1:
                return False
    return True


def main():
    #global screen
    global clock
    random_shape = ["T", "J", "O", "P", "L"]
    running = True
    current_positions = [[0 for x in range(columns)] for y in range(rows)]
    current_positions = create_shape(random_shape[random.randint(0, 4)], current_positions)
    grid = create_grid(current_positions)
    while running:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    grid = shift_right(grid)
                if event.key == pygame.K_LEFT:
                    grid = shift_left(grid)

        if hit_bottom(current_positions):
            print("hit")
            current_positions = create_shape(random_shape[random.randint(0, 4)], grid)                    #random_shape(random.randint(0, 4))
        else:

        # draw_shape(grid)
            #clock.tick(60)
            #pygame.display.flip()
            #grid = create_bottom(grid)

            grid = shift_down(grid)
            grid = create_bottom(grid)
            draw_shape(grid)

            print("here")

            time.sleep(0.2)
            current_positions = grid
    pygame.quit()


def main_menu():
    run = True
    while run:
        screen.fill((255, 255, 255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()


clock = pygame.time.Clock()
screen = pygame.display.set_mode((width+100, height+50))
pygame.display.set_caption("Tetris", "Logan Morro")

main()
