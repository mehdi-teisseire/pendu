import pygame
import menu

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Le Jeu du Pendu")
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Call the menu function to render the menu
        menu.menu(screen)

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()