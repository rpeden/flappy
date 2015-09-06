import pygame
import time

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

def replay_or_quit():
	for event in pygame.event.get([pygame.KEYDOWN, pygame.QUIT]):
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type == pygame.KEYDOWN:
			continue

		return event.key

	return None

def make_text_objects(text, font):
	text_surface = font.render(text, True, white)
	return text_surface, text_surface.get_rect()

def message_surface(text):
	small_text = pygame.font.Font('freesansbold.ttf', 20)
	large_text = pygame.font.Font('freesansbold.ttf', 100)

	title_text_surface, title_text_rectangle = make_text_objects(text, large_text)
	title_text_rectangle.center = screen_width / 2, screen_height / 2
	surface.blit(title_text_surface, title_text_rectangle)

	small_text_surface, small_text_rectangle = make_text_objects('Press any key to continue', small_text)
	small_text_rectangle.center = screen_width / 2, (screen_height / 2) + 100
	surface.blit(small_text_surface, small_text_rectangle)

	pygame.display.update()
	time.sleep(1)

	while replay_or_quit() == None:
		clock.tick()

	main()

def end_game():
	message_surface("Splat!")

def flappy(x, y, image):
	surface.blit(image, (x,y))



def main():
	game_over = False

	#location
	x = 150
	y = 200

	y_move = 5

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

main()
pygame.quit()
quit()