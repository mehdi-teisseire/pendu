import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game Title")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
title_font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 36)

def draw_title_screen():
	screen.fill(BLACK)
	
	# Draw title
	title_text = title_font.render("Jeu du pendu", True, WHITE)
	title_rect = title_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/3))
	screen.blit(title_text, title_rect)
	
	# Draw start button
	start_text = button_font.render("Espace pour commencer", True, WHITE)
	start_rect = start_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT*2/3))
	screen.blit(start_text, start_rect)

	# Draw score button
	start_text = button_font.render('Meilleurs scores', True, WHITE)
	start_rect = start_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT*2/3 + 50))
	screen.blit(start_text, start_rect)
	

	# Draw exit button
	start_text =button_font.render('Quitter', True, WHITE)
	start_rect = start_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT*2/3 + 100))
	screen.blit(start_text, start_rect)
	 
	pygame.display.flip()
def main():
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					print("Game would start here")
					# Game here
				elif event.key == pygame.K_ESCAPE:
					running = False
		
		draw_title_screen()

	pygame.quit()
	sys.exit()

if __name__ == "__main__":
	main()