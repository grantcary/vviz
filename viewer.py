import pygame

pygame.init()

window = pygame.display.set_mode((300, 300))
pygame.display.set_caption('VViz')
window.fill((0, 0, 255))
pygame.display.flip()

def color_switcher(click):
    return (255, 0, 0) if click % 2 == 0 else (0, 0, 255)

click = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            click += 1
        if event.type == pygame.QUIT:
            running = False


    window.fill((0, 0, 0))
    pygame.draw.circle(window, color_switcher(click), pygame.mouse.get_pos(), 7, 0)
    pygame.display.update()