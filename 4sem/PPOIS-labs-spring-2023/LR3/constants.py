import pygame

GAMENAME = "Boss Planet"
GRIDSIZE = 10
SCREENSIZE = 600
FONTSIZE = int(SCREENSIZE*(4/75))
SCOREBOARDRATIO = 0.5 #Changing this may stretch the scoreboard
FPS = 60
INROW = 3
MOVERATIO = 0.05
FALLSTARTRATIO = 0.05
ACCELERATION = 1.025
CANDYSIZE = 0.9 #Percentage of CELLSIZE
LINESIZE = 0.04 #Percentage of CELLSIZE
LINECOLOR = (100,100,100)
BGCOLOR = (50,25,50)
SCOREBOARDCOLOR = (250,150,150)
SCORECOLOR = (255,255,255)

def set_gridsize(value):
    global GRIDSIZE, CELLSIZE, FALLSPEED, MOVESPEED, OFFSET,MERCURY, MARS, EARTH, JUPITAR, NEPTUNE, VENUS, TEXTURES
    GRIDSIZE = value
    CELLSIZE = SCREENSIZE / GRIDSIZE
    FALLSPEED = CELLSIZE * FALLSTARTRATIO
    MOVESPEED = CELLSIZE * MOVERATIO
    OFFSET = (CELLSIZE - (CELLSIZE * CANDYSIZE)) / 2
    MERCURY = pygame.transform.scale(toScaleMercury, (int(CELLSIZE * CANDYSIZE), int(CELLSIZE * CANDYSIZE)))
    MARS = pygame.transform.scale(toScaleMars, (int(CELLSIZE * CANDYSIZE), int(CELLSIZE * CANDYSIZE)))
    EARTH = pygame.transform.scale(toScaleEarth, (int(CELLSIZE * CANDYSIZE), int(CELLSIZE * CANDYSIZE)))
    JUPITAR = pygame.transform.scale(toScaleJupitar, (int(CELLSIZE * CANDYSIZE), int(CELLSIZE * CANDYSIZE)))
    NEPTUNE = pygame.transform.scale(toScaleNeptune, (int(CELLSIZE * CANDYSIZE), int(CELLSIZE * CANDYSIZE)))
    VENUS = pygame.transform.scale(toScaleVenus, (int(CELLSIZE * CANDYSIZE), int(CELLSIZE * CANDYSIZE)))
    TEXTURES = [EARTH, MARS, VENUS, JUPITAR, NEPTUNE, MERCURY]

#Const based on above info
CELLSIZE = SCREENSIZE / GRIDSIZE
FALLSPEED = CELLSIZE*FALLSTARTRATIO
MOVESPEED = CELLSIZE*MOVERATIO
OFFSET = (CELLSIZE-(CELLSIZE*CANDYSIZE))/2
SCOREBOARDSIZE = SCOREBOARDRATIO * SCREENSIZE

VIRSCORELOCATION = (3,5.5) #X between 0 and 20. Y between 0 and 40.
VIRHISCORELOCATION = (3,20)
SCORELOCATION = ((SCOREBOARDSIZE/20)*VIRSCORELOCATION[0], (SCREENSIZE/40)*VIRSCORELOCATION[1])
HISCORELOCATION = ((SCOREBOARDSIZE/20)*VIRHISCORELOCATION[0], (SCREENSIZE/40)*VIRHISCORELOCATION[1])
SCORESTARTSIZE = (200,100)

#Textures
toScaleMercury = pygame.image.load("circle/1.png")
toScaleMars = pygame.image.load("circle/2.png")
toScaleEarth = pygame.image.load("circle/3.png")
toScaleJupitar = pygame.image.load("circle/4.png")
toScaleNeptune = pygame.image.load("circle/5.png")
toScaleVenus = pygame.image.load("circle/6.png")

toScaleScoreboard = pygame.image.load("Scoreboard.png")

MERCURY = pygame.transform.scale(toScaleMercury, (int(CELLSIZE*CANDYSIZE), int(CELLSIZE*CANDYSIZE)))
MARS = pygame.transform.scale(toScaleMars, (int(CELLSIZE*CANDYSIZE), int(CELLSIZE*CANDYSIZE)))
EARTH = pygame.transform.scale(toScaleEarth, (int(CELLSIZE*CANDYSIZE), int(CELLSIZE*CANDYSIZE)))
JUPITAR = pygame.transform.scale(toScaleJupitar, (int(CELLSIZE*CANDYSIZE), int(CELLSIZE*CANDYSIZE)))
NEPTUNE = pygame.transform.scale(toScaleNeptune, (int(CELLSIZE*CANDYSIZE), int(CELLSIZE*CANDYSIZE)))
VENUS = pygame.transform.scale(toScaleVenus, (int(CELLSIZE*CANDYSIZE), int(CELLSIZE*CANDYSIZE)))

SCOREBOARDTEX = pygame.transform.scale(toScaleScoreboard, (int(SCOREBOARDSIZE), SCREENSIZE))


TEXTURES = [EARTH, MARS, VENUS, JUPITAR, NEPTUNE, MERCURY]