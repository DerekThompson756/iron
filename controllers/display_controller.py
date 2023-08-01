import pygame
from controllers.event_controller import event_listener
from app.map.grid import Grid
from app.menu.cursor import Cursor


ZOOM = 4
SQUARE_SIZE = (16,16)
MAP_SIZE = (15, 10)
grid = Grid(MAP_SIZE[0], MAP_SIZE[1])
cursor = Cursor(MAP_SIZE,SQUARE_SIZE)
screen_res = (MAP_SIZE[0] * 16 , MAP_SIZE[1] * 16 )
display_res = (MAP_SIZE[0] * 16 * ZOOM, MAP_SIZE[1] * 16 * ZOOM)



def draw(display):
    display.fill('white')
    grid.draw(display)
    cursor.draw(display)
    pygame.display.update()


def game():


    display_win = pygame.display.set_mode(display_res)
    screen = pygame.Surface(screen_res)
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(cursor)
    clock = pygame.time.Clock()
    

    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        event_listener(cursor)

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