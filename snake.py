import pygame
import time
import random
from time import sleep
from random import randint
pygame.init()

font = pygame.font.SysFont('sans', 30)
score = 0
screen = pygame.display.set_mode((600,600))
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

pausing = False
running = True
clock = pygame.time.Clock()
#starting position of the snakes
snakes = [[19,19]]

#direction of the snakes
direction = 'LEFT'

#apple
apple = [randint(0,19), randint(0,19)]
while running:

	clock.tick(10)
	screen.fill(BLACK)

	#draw grid and snake's pos
	#for i in range(1, 20, 1):
		#pygame.draw.line(screen, WHITE, (30 * i, 0), (30 * i, 600))
		#pygame.draw.line(screen, WHITE, (0, 30 * i), (600, 30 * i))
	#draw snakes
	for snake in snakes:
		pygame.draw.rect(screen, GREEN, (snake[0]*30, snake[1]*30, 30, 30))
	#draw an apple
		pygame.draw.rect(screen, RED, (apple[0]*30, apple[1]*30, 30, 30))

	#tail of the snakes
	tail_x = snakes[0][0]
	tail_y = snakes[0][1]

	# Snake move + check crash
	if direction == "right":
		if snakes[-1][0] == 19:
			text = font.render("Game over, score: " + str(score), True, WHITE)
			press_space = font.render("Press Space to continue", True, WHITE)
			pausing = True
			screen.blit(text, (200,200))
			screen.blit(press_space, (200,300))
		else:
			snakes.append([snakes[-1][0]+1, snakes[-1][1]])
			snakes.pop(0)
	if direction == "left":
		if snakes[-1][0] == 0:
			text = font.render("Game over, score: " + str(score), True, WHITE)
			press_space = font.render("Press Space to continue", True, WHITE)
			pausing = True
			screen.blit(text, (200,200))
			screen.blit(press_space, (200,300))
		else:
			snakes.append([snakes[-1][0]-1, snakes[-1][1]])
			snakes.pop(0)
	if direction == "up":
		if snakes[-1][1] == 0:
			text = font.render("Game over, score: " + str(score), True, WHITE)
			press_space = font.render("Press Space to continue", True, WHITE)
			pausing = True
			screen.blit(text, (200,200))
			screen.blit(press_space, (200,300))
		else:
			snakes.append([snakes[-1][0], snakes[-1][1]-1])
			snakes.pop(0)
	if direction == "down":
		if snakes[-1][1] == 19:
			text = font.render("Game over, score: " + str(score), True, WHITE)
			press_space = font.render("Press Space to continue", True, WHITE)
			pausing = True
			screen.blit(text, (200,200))
			screen.blit(press_space, (200,300))
		else:
			snakes.append([snakes[-1][0], snakes[-1][1]+1])
			snakes.pop(0)
	#when snake eats the apple
	if tail_x == apple[0] and tail_y == apple[1]:
		snakes.insert(0, [tail_x, tail_y])
		apple = [randint(0,19), randint(0,19)]
		score += 1
	#click the mouse
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	#snake moves in a fixed direction! 
		if event.type == pygame.KEYDOWN:
			
			if event.key == pygame.K_UP and direction != "down":
				direction = "up"
			if event.key == pygame.K_DOWN and direction != "up":
				direction = "down"
			if event.key == pygame.K_LEFT and direction != "right":
				direction = "left"
			if event.key == pygame.K_RIGHT and direction != "left":
				direction = "right"
			if event.key == pygame.K_SPACE and pausing == True:
				pausing = False
				snakes = [[5,10]]
				apple = [randint(0,19), randint(0,19)]
				score = 0
		time.sleep(0.03)

	pygame.display.flip()
pygame.quit()
