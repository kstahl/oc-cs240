# Kattie Stahl
# Date: 09-22-12
# Lab01.py
# Description: Use PyGame to draw the Olympic Flag with a pale blue background4

import pygame

pygame.init()

## Set Screen Size
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

## Create flag parameters
flag_width, flag_height = 360, 240
flag = pygame.Rect((width - flag_width)/2, (height - flag_height)/2, flag_width, flag_height)

## Create Image onto Flag Picture
olympics = pygame.image.load("olympics.jpg").convert_alpha()
olympics_rect = olympics.get_rect()


## Colors of Rings and Flag
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 205)
yellow = pygame.Color(255, 255, 0)
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 100, 0)
red = pygame.Color(255, 0, 0)

## Sets Horizontal and Vertical Variables
horizontal = 1
vertical = 3

## Main Game Loop, continues until user exits
run = True
while run:
           
    ## Draws an Olympic Flag on a light blue background
    screen.fill((0, 191,255)) ## Deep Sky Blue background
    screen.blit(olympics, olympics_rect) ## Draws image behind flag
    pygame.draw.rect(screen, white, flag) ## Draws flag
    pygame.draw.circle(screen, blue, (200, 200), 50, 5) ## Draws First Circle - Blue
    pygame.draw.circle(screen, yellow, (255, 260), 50, 5) ## Draws Second Circle - Yellow
    pygame.draw.circle(screen, black, (310, 200), 50, 5) ## Draws Third Circle - Black
    pygame.draw.circle(screen, green, (365, 260), 50, 5) ## Draws Fourth Circle - Green
    pygame.draw.circle(screen, red, (415, 200), 50, 5) ## Draws Fifth Circle - Red

    ## Rotation and movement of the picture
    olympics_rect[0] += horizontal
    olympics_rect[1] += vertical

    if olympics_rect.right >= width:
        horizontal = -1
    elif olympics_rect.left <= 0:
        horizontal = 1
    if olympics_rect.bottom >= height:
        vertical = -3
    elif olympics_rect.top <= 0:
        vertical = 3
    
    ## Flips to the surface
    pygame.display.flip()

    ## Exits program by hitting the 'x' or pushing q
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            run = False 