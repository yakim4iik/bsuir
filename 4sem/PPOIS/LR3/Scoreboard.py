import pygame
import constants

class Scoreboard:

    score = 0
    hiScore = -1
    font = -1

    def __init__(self):
        self.font = pygame.font.Font('OpenSans-Regular.ttf', constants.FONTSIZE)
        fs = open("HiScore.txt", "r")
        self.hiScore = int(fs.read())
        fs.close()

    def drawScores(self, screen):
        text = self.font.render(str(self.score), True, constants.SCORECOLOR)
        textRec = text.get_rect()
        screen.blit(text, (constants.SCREENSIZE+constants.SCORELOCATION[0],constants.SCORELOCATION[1],100,50))

        text = self.font.render(str(self.hiScore), True, constants.SCORECOLOR)
        textRec = text.get_rect()
        screen.blit(text, (constants.SCREENSIZE+constants.HISCORELOCATION[0],constants.HISCORELOCATION[1],100,50))

    
    def updateHiScore(self):
        if (self.score>self.hiScore):
            self.hiScore = self.score
            fs = open("HiScore.txt", "w")
            fs.write(str(self.score))
            fs.close()

    def draw(self, screen):
        #pygame.draw.rect(screen, constants.SCOREBOARDCOLOR, (constants.SCREENSIZE, 0, constants.SCOREBOARDSIZE, constants.SCREENSIZE))
        screen.blit(constants.SCOREBOARDTEX, (constants.SCREENSIZE, 0))
        self.drawScores(screen)