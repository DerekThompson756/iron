# Example file showing a basic pygame "game loop"
import pygame
from app.map.grid import Grid

# pygame setup
pygame.init()

ZOOM = 4
MAP_SIZE = (15, 10)
screen_res = (MAP_SIZE[0] * 16 , MAP_SIZE[1] * 16 )
display_res = (MAP_SIZE[0] * 16 * ZOOM, MAP_SIZE[1] * 16 * ZOOM)
print(screen_res)

screen = pygame.display.set_mode(screen_res)
display_win = pygame.display.set_mode(display_res)
clock = pygame.time.Clock()

grid = Grid(MAP_SIZE[0], MAP_SIZE[1])

def draw(display):
    display.fill('white')
    grid.draw(display)
    pygame.display.update()

if __name__ == "__main__":
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        # screen.fill("dark green")

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        draw(screen)

        clock.tick(60)  # limits FPS to 60

    pygame.quit()