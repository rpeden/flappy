import pygame

black = (0,0,0)
white = (255,255,255)

pygame.init()

surface = pygame.display.set_mode((800,400))
pygame.display.set_caption("Flappy")
clock = pygame.time.Clock()

#load image
img = pygame.image.load('flappy.png')
#location
x = 150
y = 200

y_move = 5

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

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()