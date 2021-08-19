import pygame
import random
import time
import numpy as np
#globals

pygame.init()
pygame.font.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
block_size = 28
height = 800
width = 500
columns = 10
rows = 25
score = 0


def create_grid(current_positions):  # Converts Current positions on 2d array to the grid
    grid = [[0 for i in range(columns)] for j in range(rows)]
    for i in range(columns):
        for j in range(rows):
            if current_positions[j][i] == 1:
                grid[j][i] = 1
            else:
                grid[j][i] = 0
    return grid


def check_loser(current_positions):   # if the top row has a block in it, it returns true for loser
    for i in range(columns):
        if current_positions[0][i] == 2:
            return True
    return False


def create_shape(shape, current_positions):  # Generates different tetris shapes at the top of the grid
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
    if shape == "lL":
        current_positions[0][4] = 1
        current_positions[1][4] = 1
        current_positions[2][4] = 1
        current_positions[3][4] = 1
    if shape == "Z":
        current_positions[0][4] = 1
        current_positions[0][3] = 1
        current_positions[1][4] = 1
        current_positions[1][5] = 1
    if shape == "Q":
        current_positions[1][4] = 1
        current_positions[1][3] = 1
        current_positions[1][5] = 1
        current_positions[0][5] = 1
    if shape == "bQ":
        current_positions[1][4] = 1
        current_positions[1][3] = 1
        current_positions[1][5] = 1
        current_positions[0][3] = 1
    if shape == ".":
        current_positions[0][4] = 1
    if shape == "l.":
        current_positions[0][4] = 1
        current_positions[1][4] = 1

    return current_positions


def shift_down(current_positions):  # drops the tetris shape
    for i in range(columns):
        for j in range(rows-1, -1, -1):
            if (current_positions[j][i] == 1) and j != (rows-1) and not hit_bottom(current_positions):
                current_positions[j][i] = 0
                current_positions[j+1][i] = 1

    return current_positions


def draw_shape(grid):   # draws the grid, with color, and based off the value of the coordinate,
                        # make it white, green or red
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


def create_bottom(current_positions):   # creates a bottom once the tetris shape hits the
                                        # furtherst down row, or another block
    for i in range(columns):
        for j in range(rows-1, -1, -1):
            if current_positions[j][i] == 1 and j == rows-1:
                current_positions[j][i] = 2
                current_positions = convert(current_positions)
            if j != (rows-1) and current_positions[j][i] == 1 and current_positions[j+1][i] == 2:
                current_positions[j][i] = 2
                current_positions = convert(current_positions)
    return current_positions


def convert(current_positions):   # converts everything to a stationary block, helpful once we find out if
                                  # the tetris shape hit a bottom, allows for quick conversion

    for i in range(columns):
        for j in range(rows-1):
            if current_positions[j][i] == 1:
                current_positions[j][i] = 2
    return current_positions


def shift_point(current_positions, row):    # this function is called after we obtain a point, shifts
                                            # down the blocks above the row where the point was earned
    for i in range(columns):
        for j in range(row, -1, -1):
            if current_positions[j][i] == 2 and j != rows-1:
                current_positions[j][i] = 0
                current_positions[j+1][i] = 2
    return current_positions


def remove_row(current_positions, j):   # deletes a row given by j
    for i in range(columns):
        current_positions[j][i] = 0
    return current_positions


def check_for_point(current_positions):   # counts the amount of blocks per row, if the amount is the whole
                                          # row, we pass True, and the row where the point was found
    count = 0
    for j in range(rows):
        for i in range(columns):
            if current_positions[j][i] == 2:
                count += 1
        if count == 10:
            print('true and j')
            return True, j
        count = 0
    return False, 0


def shift_right(current_positions):   # shifts falling tetris block to right
    for i in range(columns-1, -1, -1):
        for j in range(rows-1):
            if current_positions[j][i] == 1 and i != columns-1 and current_positions[j][i+1] != 2:
                current_positions[j][i] = 0
                current_positions[j][i+1] = 1
            if current_positions[j][i] == 1 and i == columns-1:
                return current_positions
    return current_positions


def shift_left(current_positions):   # # shifts falling tetris block to left
    for i in range(columns):
        for j in range(rows-1):
            if current_positions[j][i] == 1 and i != 0:
                current_positions[j][i] = 0
                current_positions[j][i-1] = 1
            if current_positions[j][i] == 1 and i == 0:
                return current_positions
    return current_positions



def hit_bottom(current_positions):   # if bottom was hit, all blocks are converted to value of 2,
                                     # this function checks weather any blocks have a
                                     # value of 1, to determine if we hit the bottom or not
    for i in range(columns):
        for j in range(rows):
            if current_positions[j][i] == 1:
                return False
    return True


def main():
    global score
    global clock
    font1 = pygame.font.Font('freesansbold.ttf', 15)
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('SCORE:', True, GREEN, BLACK)
    textRect = text.get_rect()
    textRect.center = (400, 100)

    random_shape = ["J", "O", "P", "L", "Z", "lL", "Q", "bQ", ".", "l."]
    running = True
    current_positions = [[0 for x in range(columns)] for y in range(rows)]
    current_positions = create_shape(random_shape[random.randint(0, 9)], current_positions)
    grid = create_grid(current_positions)
    while running:
        points = font1.render(str(score), True, RED, BLACK)
        pointsRect = points.get_rect()
        pointsRect.center = (460, 100)
        screen.blit(text, textRect)
        screen.blit(points, pointsRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    grid = shift_right(grid)
                if event.key == pygame.K_LEFT:
                    grid = shift_left(grid)
        if hit_bottom(current_positions):
            current_positions = create_shape(random_shape[random.randint(0, 9)], grid)
        else:
            draw_shape(grid)
            grid = create_bottom(grid)
            result = check_for_point(grid)
            # print(result[0])
            # print(result[1])
            if result[0]:
                score += 1
                print(score)
                row = result[1]
                grid = remove_row(grid, row)
                grid = shift_point(grid, row)

            grid = shift_down(grid)

            if check_loser(grid):
                print("loser")
                main_menu()

            time.sleep(0.15)
            current_positions = grid
    pygame.quit()


def main_menu():
    global score
    print(score)
    run = True
    screen.fill((0, 0, 0))
    font1 = pygame.font.Font('freesansbold.ttf', 20)
    font = pygame.font.Font('freesansbold.ttf', 20)
    points = font.render(str(score), True, RED, BLACK)
    score = font1.render("YOU LOST WITH A SCORE:", True, RED, BLACK)
    scoreRect = score.get_rect()
    pointsRect = points.get_rect()
    pointsRect.center = (250, 500)
    scoreRect.center = (250, 400)
    screen.blit(score, scoreRect)
    screen.blit(points, pointsRect)
    while run:
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
