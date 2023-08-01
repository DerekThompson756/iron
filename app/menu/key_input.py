import pygame

def arrow_keys(event):
    if event.key == pygame.K_UP:
        return 'up'
    if event.key == pygame.K_DOWN:
        return 'down'
    if event.key == pygame.K_LEFT:
        return 'left'
    if event.key == pygame.K_RIGHT:
        return 'right'