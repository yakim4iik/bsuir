import pygame
import pygame.gfxdraw
import constants

class JewelPiece:

    x = -1
    y = -1
    yGap = 0
    xGap = 0
    accel = 1
    isFalling = False
    colorNum = -1

    def __init__(self, x, y, colorNum):
        self.x = x
        self.y = y
        self.colorNum = colorNum
    
    def updatePos(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(constants.TEXTURES[self.colorNum], (int(self.x*constants.CELLSIZE+constants.OFFSET + self.xGap), int(self.y*constants.CELLSIZE+constants.OFFSET + self.yGap)))