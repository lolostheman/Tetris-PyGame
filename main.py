import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

blocksize = 50

class tetrisBlocks:
    def __init__(self, shape, length, color):
        self.length = length
        self.shape = shape
        self.color = color
    def blockGenerate(self):
        if self.shape == 'T':
            return [0, 1, 1, 1], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]
        if self.shape == 'L':
            return [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]
        if self.shape == 'J':
            return [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 0, 0]
        if self.shape == 'P':
            return [0, 0, 1, 1], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]
        if self.shape == 'O':
            return [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]


grid = []
for row in range(13):
    grid.append([])
    for column in range(10):
        grid[row].append(0)


pygame.init()
screen = pygame.display.set_mode([500, 800])
clock = pygame.time.Clock()


def drawBlock(shape):
    running = True
    if shape == 'T':
        grid[0][4] = 1
        grid[0][3] = 1
        grid[0][5] = 1
        grid[1][4] = 1
        grid[2][4] = 1
    while running:
        screen.fill(BLACK)
        for row in range(13):

            for column in range(10):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                pygame.draw.rect(screen, color,
                                 [(5 + blocksize) * column + 5, (5 + blocksize) * row + 5, blocksize, blocksize])
        shift = 0

        for row in range(13):
            for column in range(10):
                if shift < 10:
                    if grid[row][column] == 1:
                        grid[row][column] = 0
                        grid[row+1][column] = 1
            shift += 1




        clock.tick(1)
        pygame.display.flip()
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                running = False




drawBlock('T')
pygame.quit()


# running = True
#
# while running:
#     screen.fill(BLACK)
#     for row in range(13):
#         for column in range(10):
#             color = WHITE
#             if grid[row][column] == 1:
#                 color = GREEN
#             pygame.draw.rect(screen, color, [(5 + blocksize) * column + 5, (5 + blocksize) * row + 5, blocksize, blocksize])
#     clock.tick(60)
#     pygame.display.flip()












# running = True
#
# while running:
#     createMap()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.display.update()








