import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My Game Screen")

white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)

font = pygame.font.SysFont("Arial", 36)
text_surface = font.render("Hello Pygame!", True, black)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    pygame.draw.rect(screen, blue, (150, 200, 200, 100))

    screen.blit(text_surface, (140, 100))

    pygame.display.flip()

pygame.quit()