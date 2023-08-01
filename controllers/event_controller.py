import pygame
from app.menu.key_input import arrow_keys

def event_listener(cursor):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            key_input = arrow_keys(event)
            cursor.move(key_input)

def event_initialize():
    #do stuff
    print()