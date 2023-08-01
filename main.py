# Example file showing a basic pygame "game loop"
import pygame
from app.map.grid import Grid
from app.menu.cursor import Cursor
from app.menu.key_input import arrow_keys

# pygame setup
pygame.init()

ZOOM = 4
MAP_SIZE = (15, 10)
screen_res = (MAP_SIZE[0] * 16 , MAP_SIZE[1] * 16 )
display_res = (MAP_SIZE[0] * 16 * ZOOM, MAP_SIZE[1] * 16 * ZOOM)
print(display_res)

display_win = pygame.display.set_mode(display_res)
screen = pygame.Surface(screen_res)

clock = pygame.time.Clock()

moving_sprites = pygame.sprite.Group()

grid = Grid(MAP_SIZE[0], MAP_SIZE[1])
cursor = Cursor(MAP_SIZE, 16, 16)

moving_sprites.add(cursor)

def draw(display):
    display.fill('white')
    grid.draw(display)
    cursor.draw(display)
    pygame.display.update()

if __name__ == "__main__":
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                key_input = arrow_keys(event)
                cursor.move(key_input)

        # fill the screen with a color to wipe away anything from last frame
        # screen.fill("dark green")

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        draw(screen)

        #Window scaling
        scaled_win = pygame.transform.scale(screen, display_win.get_size())
        moving_sprites.update()
        display_win.blit(scaled_win, (0,0))
        pygame.display.flip

        clock.tick(60)  # limits FPS to 60

    pygame.quit()