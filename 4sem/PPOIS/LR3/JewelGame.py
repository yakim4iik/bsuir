from Board import Board
from Scoreboard import Scoreboard
import pygame
import math
import constants
from enum import Enum
import sys
import time

pygame.init()

class GameState(Enum):
    PLAYING = 1
    WELCOME = 2
    LEVEL = 3

class EventType(Enum):
    TIMEOUT = pygame.USEREVENT
    

class Button():
    def __init__(self, x, y, width, height, font, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

    def process(self, screen):
        mousePos = pygame.mouse.get_pos()
        
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)
        
#Vars
screen = pygame.display.set_mode((constants.SCREENSIZE + int(constants.SCOREBOARDSIZE),constants.SCREENSIZE))
pygame.display.set_caption(constants.GAMENAME)
pygame.display.set_icon(constants.JUPITAR)
clock = pygame.time.Clock()
currentState = GameState.WELCOME
scoreBoard = Scoreboard()
currentBoard = Board(scoreBoard)
currentBoard.randomize()
running = True
clickPos = (0,0)

medium_font = pygame.font.SysFont(None, 50)

start_button = Button(250, 100, 400, 100, medium_font, buttonText="Start Normal Game", onclickFunction=lambda: start_game())
start_timeout_button = Button(250, 250, 400, 100, medium_font, buttonText="Start Timeout Game", onclickFunction=lambda: start_with_timeout_game(10))
quit_button = Button(250, 400, 400, 100, medium_font, buttonText="Quit", onclickFunction=lambda: sys.exit(1))

button_1 = Button(250, 250, 400, 50, medium_font, buttonText="Level 1", onclickFunction=lambda: start_level(6))
button_2 = Button(250, 350, 400, 50, medium_font, buttonText="Level 2", onclickFunction=lambda: start_level(8))
button_3 = Button(250, 450, 400, 50, medium_font, buttonText="Level 3", onclickFunction=lambda: start_level(10))

def start_game():
    global currentState
    currentState = GameState.LEVEL

def start_with_timeout_game(level):
    global currentState
    global currentBoard
    constants.set_gridsize(level)
    currentBoard = Board(scoreBoard)
    pygame.time.set_timer(EventType.TIMEOUT.value, 2 * 5 * 1000)
    currentState = GameState.PLAYING

def start_level(level):
    global currentBoard
    global currentState
    constants.set_gridsize(level)
    currentBoard = Board(scoreBoard)
    currentState = GameState.PLAYING


    

def update():
    global running
    global clickPos
    global currentState
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        currentState = GameState.WELCOME
        scoreBoard.score = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == EventType.TIMEOUT.value:
            currentState = GameState.WELCOME
            scoreBoard.score = 0

        elif (event.type==1025):
            if (event.pos[0]<constants.SCREENSIZE):
                xPos = math.floor(event.pos[0]/constants.CELLSIZE)
                yPos = math.floor(event.pos[1]/constants.CELLSIZE)
                clickPos = (xPos, yPos)
        elif (event.type==1026 and currentBoard.swap1 == -1):
            if (event.pos[0]<constants.SCREENSIZE):
                xPos = math.floor(event.pos[0]/constants.CELLSIZE)
                yPos = math.floor(event.pos[1]/constants.CELLSIZE)
                xOff = xPos-clickPos[0]
                yOff = yPos-clickPos[1]
                dist = math.hypot(xOff, yOff)
                if (dist>0.5):
                    if (abs(xOff)>abs(yOff)):
                        if (xOff>0):
                            currentBoard.startSwap(clickPos[0], clickPos[1], clickPos[0]+1, clickPos[1], True)
                        else:
                            currentBoard.startSwap(clickPos[0]-1, clickPos[1], clickPos[0], clickPos[1], True)
                    else:
                        if (yOff>0):
                            currentBoard.startSwap(clickPos[0], clickPos[1], clickPos[0], clickPos[1]+1, False)
                        else:
                            currentBoard.startSwap(clickPos[0], clickPos[1]-1, clickPos[0], clickPos[1], False)

    currentBoard.update()


def draw():
    screen.fill(constants.BGCOLOR)
    if currentState == GameState.WELCOME:
        start_button.process(screen)
        start_timeout_button.process(screen)
        quit_button.process(screen)
    elif currentState == GameState.LEVEL:
        button_1.process(screen)
        button_2.process(screen)
        button_3.process(screen)
    elif currentState == GameState.PLAYING:
        currentBoard.draw(screen)
        scoreBoard.draw(screen)


while running:
    clock.tick(constants.FPS)
    update()
    draw()
    pygame.display.update()
pygame.quit()
