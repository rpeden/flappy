import pygame

black = (0,0,0)
white = (255,255,255)

pygame.init()

screen_width = 800
screen_height = 500

surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy")
clock = pygame.time.Clock()

#load image
img = pygame.image.load('flappy.png')
#location
x = 150
y = 200

y_move = 5

def end_game():
	pygame.quit()
	quit()

def flappy(x, y, image):
	surface.blit(image, (x,y))

game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				y_move = -5
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				y_move = 5

	y += y_move
	surface.fill(black)
	flappy(x,y,img)

	if y > screen_height or y < 0:
		end_game()

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()