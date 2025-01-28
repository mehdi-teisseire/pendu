import pygame
import menu

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((425, 600))
    pygame.display.set_caption("Le Jeu du Pendu")
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        screen.fill((0, 0, 0))

        
        menu.menu(screen)

        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()