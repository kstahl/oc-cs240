## Kattie Stahl
## CS 240
## newshooter.py
##
## This program has two character that are throwing snowballs at each other.
## The Hero is the girl with the smaller snowballs, and the oponent is the boy
## with the larger snowballs. The boy oponent gets hit by the girl's snowballs
## and the girl wins.
## 


import pygame

WINDOW_TITLE = 'Snowball Fight'
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def init():
    pygame.init()
    pygame.display.set_caption(WINDOW_TITLE)

    return pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

class Hero(object):
    def __init__(self):
        self.image = pygame.image.load('chgirl.png').convert_alpha()
        self.x = 50
        self.y = 400
        self.bullets = [[100, 400], [100, 420], [100, 440]]
        self.frame = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            pygame.draw.circle(screen, (255, 255, 255), 
                                (bullet[0], bullet[1]), 4)

    def update(self, screen):
        # Update frame counter
        self.frame += 1
        # Move any existing bullets
        for bullet in self.bullets:
            bullet[1] -= 1

        # Move hero 
        self.x += 1
        if self.x > screen.get_height():
            print len(self.bullets)
            self.x = 0
        # Throw 3 more snowballs every 20 pixels  of movement
        if self.x % 100 == 0:
            self.bullets.append([self.x + 100, 250])
            self.bullets.append([self.x + 100, 270])
            self.bullets.append([self.x + 100, 290])

class Oponent(object):
    def __init__(self):
        self.image = pygame.image.load('chboy.png').convert_alpha()
        self.x = 50
        self.y = 100
        self.bullets = [[90, 250], [90, 270], [90, 290]]
        self.frame = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            pygame.draw.circle(screen, (255, 255, 255), 
                                (bullet[0], bullet[1]), 6)

    def update(self, screen):
        # Update frame counter
        self.frame += 1
        # Move any existing bullets
        for bullet in self.bullets:
            bullet[1] += 1

        # Move hero 
        self.x += 1
        if self.x > screen.get_height():
            print len(self.bullets)
            self.x = 0
        # Throw 3 more snowballs every 20 pixels  of movement
        if self.x % 100 == 0:
            self.bullets.append([self.x + 100, 250])
            self.bullets.append([self.x + 100, 270])
            self.bullets.append([self.x + 100, 290])

def init():
    width, height = 800, 600
    pygame.init()
    # Screen
    return pygame.display.set_mode((width, height))


def main(screen):
    clock = pygame.time.Clock()
    hero = Hero()
    oponent = Oponent()
    running = True
    while running:
        screen.fill((0, 0, 0)) # Redraw background
        hero.draw(screen)
        oponent.draw(screen)
        pygame.display.flip() # Display screen in window
        hero.update(screen)
        oponent.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # exit()
                running = False
        clock.tick(40)
        print "You Escaped and hit your oponent!"


screen = init()
main(screen)