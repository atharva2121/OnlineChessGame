import pygame
import os

#from Game import win

b_bishop = pygame.image.load(os.path.join("b_bishop.png"))
b_king = pygame.image.load(os.path.join("b_king.png"))
b_knight = pygame.image.load(os.path.join("b_knight.png"))
b_pawn = pygame.image.load(os.path.join("b_pawn.png"))
b_queen = pygame.image.load(os.path.join("b_queen.png"))
b_rook = pygame.image.load(os.path.join("b_rook.png"))

w_bishop = pygame.image.load(os.path.join("w_bishop.png"))
w_king = pygame.image.load(os.path.join("w_king.png"))
w_knight = pygame.image.load(os.path.join("w_knight.png"))
w_pawn = pygame.image.load(os.path.join("w_pawn.png"))
w_queen = pygame.image.load(os.path.join("w_queen.png"))
w_rook = pygame.image.load(os.path.join("w_rook.png"))

b = [b_rook, b_pawn, b_queen, b_king, b_knight, b_bishop]
w = [w_rook, w_pawn, w_queen, w_king, w_knight, w_bishop]

B = []
W = []

for img in b:
     B.append(pygame.transform.scale(img,(65, 65)))

for img in w:
     W.append(pygame.transform.scale(img, (65, 65)))


class Pieces:

    img = -1
    rect = (19, 8, 527, 520)
    startX = rect[0]
    startY = rect[1]

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False

    def moves(self):
        pass

    def isSelected(self):
        return self.selected

    def draw(self, win):
        if self.color == "w":
            drawThis = W[self.img]
        else:
            drawThis = B[self.img]

        x = self.startX + (self.col * self.rect[2] / 8)
        y = self.startY + (self.row * self.rect[2] / 8)

        win.blit(drawThis, (x, y))


class Rook(Pieces):
    img = 0


class Pawn(Pieces):
        img = 1


class Queen(Pieces):
    img = 2


class King(Pieces):
    img = 3


class Knight(Pieces):
    img = 4


class Bishop(Pieces):
    img = 5
