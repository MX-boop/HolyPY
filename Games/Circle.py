from math import pi, sin, cos
import pygame

RES = WIDTH, HEIGHT = 800, 800
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 20, bold=True)

running = True
paused = False
theta = 0.0

while running:
    screen.fill((0, 0, 0))

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    if not paused:
        x = int(cos(theta) * 400 + 400)
        y = int(sin(theta) * 400 + 400)
        pygame.draw.rect(screen, WHITE, (x, y, 5, 5))

        theta += 0.1

        if theta >= pi * 2:
            theta = 0.0

    pygame.display.flip()

pygame.quit()