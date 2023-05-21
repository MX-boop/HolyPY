import pygame

RES = WIDTH, HEIGHT = 800, 800
WHITE = (255, 255, 255)

# Define the pixel size
PIXEL_SIZE = 10

pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 20, bold=True)

running = True
paused = False

while running:
    screen.fill((0, 0, 0))

    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_UP:
                PIXEL_SIZE += 1
            elif event.key == pygame.K_DOWN:
                PIXEL_SIZE = max(1, PIXEL_SIZE - 1)

    if not paused:
        for i in range(0, WIDTH, PIXEL_SIZE):
            for j in range(0, HEIGHT, PIXEL_SIZE):
                pygame.draw.rect(screen, WHITE, (i, j, PIXEL_SIZE, PIXEL_SIZE))
                pygame.display.flip()
pygame.quit()