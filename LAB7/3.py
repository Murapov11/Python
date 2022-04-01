import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
RED = (255, 0, 0)
x = 25
y = 25
clock = pygame.time.Clock()
# Frame per second
FPS = 30

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x = x + 20
            if event.key == pygame.K_DOWN:
                y = y + 20
            if event.key == pygame.K_UP:
                y = y - 20
            if event.key == pygame.K_LEFT:
                x = x - 20
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 20
    if pressed[pygame.K_DOWN]:
        y += 20
    if pressed[pygame.K_LEFT]:
        x -= 20
    if pressed[pygame.K_RIGHT]:
        x += 20  
    if (x < 25):
        x = 25
    if (y < 25):
        y = 25
    if (x > 475):
        x = 475
    if (y > 475):
        y = 475
    screen.fill((255,255,255))
    pygame.draw.circle(screen, RED, (x, y), 25)
    pygame.display.flip()
    clock.tick(FPS)