import pygame
from Nodes import Node
from aStarAlgo import aStar

pygame.init()

GREY = (128, 128, 128)
BLACK = (0, 0, 0)
HEIGHT, WIDTH = 500, 500
window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("A* (A star) Algorithm")



def algo(grid,draw, start, end):
    aStar(grid,draw, start, end)


def createGrid(row, width):

    grid = []
    node_width = width // row
    for i in range(row):
        grid.append([])
        for j in range(row):
            grid[i].append(Node(i, j, node_width, row))
    return grid


def gridLines(window, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(window, BLACK, (0, i * gap), (width, i * gap))
        pygame.draw.line(window, BLACK, (i * gap, 0), (i * gap, width))


def draw(window, grid, rows, width):
    for row in grid:
        for node in row:
            node.draw(window)
    gridLines(window, rows, width)
    pygame.display.update()


def clickedPosition(position, rows, width):
    gap = width // rows
    x, y = position
    row, column = x // gap, y // gap
    return (row, column)


def main(window, WIDTH):
    ROWS = 10
    grid = createGrid(ROWS, WIDTH)

    start, end = None, None
    started = False
    run = True

    started = False
    while run:
        draw(window, grid, ROWS, WIDTH)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                row, column = clickedPosition(position, ROWS, WIDTH)
                node = grid[row][column]
                if not start and node != end:
                    start = node
                    start.makeStartNode()
                elif not end and node != start:
                    end = node
                    end.makeEndNode()
                elif node != start and node != end:
                    node.makeObstacle()

            elif pygame.mouse.get_pressed()[2]:
                position = pygame.mouse.get_pos()
                row, column = clickedPosition(position, ROWS, WIDTH)
                node = grid[row][column]
                node.resetNode()
                if node == start:
                    start = None
                if node == end:
                    end = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    started = True
                    for row in grid:
                        for node in row:
                            node.updateNeighbors(grid)
                    algo(lambda: draw(window, grid, ROWS, WIDTH), grid, start, end)
                    started = False
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = createGrid(ROWS, WIDTH)
                    draw(window, grid, ROWS, WIDTH)

    pygame.quit()

main(window, WIDTH)
