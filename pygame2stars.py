import random
import pygame

width, height = 800, 600

def init():
    pygame.init() # Initialized pygame module

    # Screen
    return pygame.display.set_mode((width, height))

def draw_space(surface, stars):
    surface.fill((0, 0, 0)) # Draw the vacuum of space
    for s in stars:
        if s[2] == 3:
            star = pygame.Color(255, 255, 255)
        elif s[2] == 2:
            star = pygame.Color(200, 200, 255)
            # star = pygame.Color(0, 0, 200)
        elif s[2] == 1:
            star = pygame.Color(255, 170, 170)
            # star = pygame.Color(200, 0, 0)
        pygame.draw.circle(surface, star, s[:2], s[2])

def build_space(screen):
    # Get a new surface and its parameters
    space = screen.copy()
    width, height = screen.get_size()

    stars = []
    for star in range(60):
        x = random.randint(0, width)
        y = random.randint(0, height)
        rand = random.randint(1, 10)
        if rand <= 6:
            r = 1
        elif rand <= 9:
            r = 2
        else:
            r = 3
        stars.append((x, y, r))
    # print stars

    draw_space(space, stars)
    return space


def main(screen):
    running = True

    space = build_space(screen)
    while running:
        screen.blit(space, (0, 0))
        pygame.display.flip() # Display screen in window

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # exit()
                running = False


screen = init()
main(screen)