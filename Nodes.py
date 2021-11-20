import pygame

HEIGHT, WIDTH = 500, 500


RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
PURPLE = (128, 0, 128)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)



class Node:
    def __init__(self, row, column, width, total_rows):
        self.row = row
        self.column = column
        self.x = row * width
        self.y = column * width
        self.color = WHITE
        self.width = width
        self.neighbors = []
        self.total_rows = total_rows

    def getPosition(self):
        return self.row, self.column

    def makeStartNode(self):
        self.color = RED

    def isStartNode(self):
        return self.color == RED

    def makeEndNode(self):
        self.color = GREEN

    def isEndNode(self):
        return self.color == GREEN

    def makeObstacle(self):
        self.color = BLACK

    def isObstacle(self):
        return self.color == BLACK

    def makeVisited(self):
        self.color = YELLOW

    def isCLosed(self):
        return self.color == YELLOW

    def makeVisiting(self):
        self.color = CYAN

    def isVisiting(self):
        return self.color == CYAN

    def makePath(self):
        self.color = BLUE

    def resetNode(self):
        self.color = WHITE

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    def updateNeighbors(self, grid):
        self.neighbors = []
        if (
            self.row < self.total_rows - 1
            and not grid[self.row + 1][self.column].isObstacle()
        ):
            self.neighbors.append(grid[self.row + 1][self.column])
        if self.row > 0 and not grid[self.row - 1][self.column].isObstacle():
            self.neighbors.append(grid[self.row - 1][self.column])
        if (
            self.column < self.total_rows - 1
            and not grid[self.row][self.column + 1].isObstacle()
        ):
            self.neighbors.append(grid[self.row][self.column + 1])
        if self.column > 0 and not grid[self.row][self.column - 1].isObstacle():
            self.neighbors.append(grid[self.row][self.column - 1])

    def __lt__(self, other):
        return False