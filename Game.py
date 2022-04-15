import pygame
import os

from Pieces import Bishop

pygame.init()

board = pygame.transform.scale(pygame.image.load(os.path.join("board_alt.png")), (550, 550))
rect = (17, 8, 527, 520)

def redraw_gameWindow():
    global win
    win.blit(board, (0, 0))
    b = Bishop(0 , 2, "w")
    b1 = Bishop(0, 5, "w")
    b.draw(win)
    b1.draw(win)

    pygame.display.update()



def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(10)
        redraw_gameWindow()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


width = 550
height = 550

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess Game")


main()
