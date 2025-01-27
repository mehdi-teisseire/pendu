import pygame

# Initialize Pygame
pygame.init()

# Constants for window dimensions
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Multi-Zone Pygame Window')

# Define the zones using pygame.Rect
zone1 = pygame.Rect(0, 0, 450, 200)         # Menu Area
zone2 = pygame.Rect(0, 200, 450, 400)       # Hangman Drawing Area
zone3 = pygame.Rect(450, 0, 450, 200)       # Letters to Guess Area
zone4 = pygame.Rect(450, 200, 450, 200)     # Input Box Area
zone5 = pygame.Rect(450, 400, 450, 200)     # Error Message Area

# Function to render the menu
def render_menu():
    pygame.draw.rect(screen, (200, 255, 200), zone1)  # Light green background for the menu
    font = pygame.font.Font(None, 36)
    text_surface = font.render('Menu', True, (0, 0, 0))  # Black text
    screen.blit(text_surface, (zone1.x + 10, zone1.y + 10))

# Function to render hangman drawing
def render_hangman():
    pygame.draw.rect(screen, (150, 150, 255), zone2)  # Light blue background for hangman area
    font = pygame.font.Font(None, 36)
    text_surface = font.render('Hangman Drawing', True, (0, 0, 0))
    screen.blit(text_surface, (zone2.x + 10, zone2.y + 10))

# Function to render letters to guess
def render_letters():
    pygame.draw.rect(screen, (255, 255, 150), zone3)  # Light yellow background for letters area
    font = pygame.font.Font(None, 36)
    text_surface = font.render('Letters to Guess', True, (0, 0, 0))
    screen.blit(text_surface, (zone3.x + 10, zone3.y + 10))

# Function to render input box
def render_input_box():
    pygame.draw.rect(screen, (255, 150, 150), zone4)  # Light red background for input area
    font = pygame.font.Font(None, 36)
    text_surface = font.render('Input Box', True, (0, 0, 0))
    screen.blit(text_surface, (zone4.x + 10, zone4.y + 10))

# Function to render error messages
def render_error_messages():
    pygame.draw.rect(screen, (255, 100, 255), zone5)  # Light purple background for error messages
    font = pygame.font.Font(None, 36)
    text_surface = font.render('Error Messages Here', True, (0, 0, 0))
    screen.blit(text_surface, (zone5.x + 10, zone5.y + 10))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen and render content
    screen.fill((255, 255, 255))  # Fill the screen with white

    render_menu()
    render_hangman()
    render_letters()
    render_input_box()
    render_error_messages()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()