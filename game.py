'''
This is a primitive tik-tak-toe game. I followed the tutorial
from AtiByte ( https://www.youtube.com/channel/UC4L3JyeL7TXQM1f3yD6iVQQ )

You can restart the game by pressing the space button,
and close it by pressing the esc.

code by arturfriedrich ( https://github.com/arturfriedrich )
inspiration by atibyte ( https://github.com/totex )
'''

import pygame
from grid import Grid

import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "400, 100"

surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic-tak-toe")

grid = Grid()

player = "X"

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                grid.get_mouse(pos[0] // 200, pos[1] // 200, player)
                if grid.switch_player:
                    if player == "X":
                        player = "O"
                    else:
                        player = "X"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_over:
                grid.clear_grid()
                grid.game_over = False
            elif event.key == pygame.K_ESCAPE:
                running = False

    surface.fill((0, 0, 0))

    grid.draw(surface)

    pygame.display.flip()