## Author: Kattie Stahl
## Date: 09-22-12
## Lab01.py
## Description: Use PyGame to draw the Olympic Flag with a pale blue 
## background

import pygame

pygame.init()

# Set screen size# Author: Kattie Stahl
# Date: 09-22-12
# Lab01.py
# Description: Use PyGame to draw the Olympic Flag with a pale blue 
# background

import pygame

pygame.init()

# Set screen size
width,height = 640,480
screen = pygame.display.set_mode((width,height))

# Create flag parameteres
flag_width, flag_height = 360, 240
flag = pygame.Rect((width - flag_width)/2, (height - flag_height)/2, flag_width, flag_height)

# Colors and Rings of teh Flag
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 205)
yellow = pygame.Color(255, 255, 0)
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 100, 0)
red = pygame.Color(255, 0, 0)

# Set horizontal and vertical variables
horizontal = 1
veritical = 3


# Main game loop that, ontinues until you exit
run = True
while run:

	# Draw Olympic Flag with Pale Blue background
	screen.fill((0,191,255))									# Draw Pale Blue Background
	pygame.draw.rect(screen, white, flag)						# Draw Flag
	pygame.draw.circle(screen, blue, (200, 200), 50, 7)				# Draw 1st circle in Blue
	pygame.draw.circle(screen, yellow, (255, 260), 50, 7)				# Draw 2nd circle in Yellow
	pygame.draw.circle(screen, black, (310, 200), 50, 7)				# Draw 3rd circle in Black
	pygame.draw.circle(screen, green, (365, 260), 50, 7)				# Draw 4th circle in Green
	pygame.draw.circle(screen, red, (415, 200), 50, 7)				# Draw 5th circle in Red

	# Flips picture onto screen
	pygame.display.flip()

	# Exists program by hitting the 'x' or by pushing q
	for event in pygame.event.get():
		if event == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
			run = False


