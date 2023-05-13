import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

grid_size = (80, 60)
cell_size = 10
grid = [[0] * grid_size[1] for _ in range(grid_size[0])]

pygame.init()
screen = pygame.display.set_mode((grid_size[0] * cell_size, grid_size[1] * cell_size))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()

def get_neighbors(x, y):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if x + i >= 0 and x + i < grid_size[0] and y + j >= 0 and y + j < grid_size[1]:
                neighbors.append((x + i, y + j))
    return neighbors

def update_grid():
    new_grid = [[0] * grid_size[1] for _ in range(grid_size[0])]
    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            num_neighbors = sum([grid[n[0]][n[1]] for n in get_neighbors(x, y)])
            if grid[x][y] == 1:
                if num_neighbors in [2, 3]:
                    new_grid[x][y] = 1
            elif grid[x][y] == 0:
                if num_neighbors == 3:
                    new_grid[x][y] = 1
    return new_grid

def draw_grid():
    screen.fill(BLACK)
    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            if grid[x][y] == 1:
                pygame.draw.rect(screen, WHITE, (x * cell_size, y * cell_size, cell_size, cell_size))

running = True
paused = False
speed = 10

# Main game loop
# To Future MX-boop
# this is the game loop
# this is the only thing you want to edit
# if you edit something else your going to break it
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_UP:
                speed += 1
            elif event.key == pygame.K_DOWN:
                speed = max(1, speed - 1)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x //= cell_size
            y //= cell_size
            grid[x][y] = 1 - grid[x][y]

    if not paused:
        grid = update_grid()

    draw_grid()

    pygame.display.flip()

    clock.tick(speed)

pygame.quit()