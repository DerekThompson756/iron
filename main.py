# Example file showing a basic pygame "game loop"
import pygame
from controllers.display_controller import game

# pygame setup
pygame.init()


if __name__ == "__main__":
    game()
    if pygame.get_init():
        print(pygame.get_init())
        pygame.QUIT()
