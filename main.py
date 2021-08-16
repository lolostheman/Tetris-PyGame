import pygame


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

def createMap():
    running = True
    while running:

        (width, height) = (300, 540)
        screen = pygame.display.set_mode((width, height))
        #pygame.display.flip()
        blockSize = 20
        for x in range(0, width, blockSize):
            for y in range(0, height, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False







# running = True
#
# while running:
#     createMap()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.display.update()

createMap()






