from JewelPiece import JewelPiece
import random
import pygame
import constants

class Board:
    grid = [[]]
    clearStage=False

    swap1 = -1
    swap2 = -1
    isHor = False
    isSwapBack = False
    scoreBoard = -1

    def __init__(self, scoreBoard):
        self.grid = [[-1 for i in range(10)] for p in range(10)]
        self.scoreBoard = scoreBoard

    def oldRandomize(self): #Delete
        for x in range(constants.GRIDSIZE):
            for y in range(constants.GRIDSIZE):
                self.grid[x][y] = JewelPiece(x,y, random.randint(0, len(constants.TEXTURES)-1))
    
    def randomize(self):
        for y in range(constants.GRIDSIZE):
            for x in range(constants.GRIDSIZE):
                toExcludeX = -1
                toExcludeY = -1
                if (x>constants.INROW-2):
                    toExcludeX = self.grid[x-(constants.INROW-1)][y].colorNum
                    for i in range(1, constants.INROW-1):
                        if (self.grid[x-i][y].colorNum != toExcludeX):
                            toExcludeX = -1
                            break
                
                if (y>constants.INROW-2):
                    toExcludeY = self.grid[x][y-(constants.INROW-1)].colorNum
                    for i in range(1, constants.INROW-1):
                        if (self.grid[x][y-i].colorNum != toExcludeY):
                            toExcludeY = -1
                            break

                posCols = [i for i in range(len(constants.TEXTURES))]
                if (toExcludeX!=-1):
                    posCols.remove(toExcludeX)
                if (toExcludeY!=toExcludeX and toExcludeY!=-1):
                    posCols.remove(toExcludeY)
                self.grid[x][y] = JewelPiece(x,y, random.choice(posCols))
    
    def checkPoint(self, x, y, colorNum, visited): #USED in floodFillDel
        if (self.grid[x][y]!=-1):
            if (colorNum==self.grid[x][y].colorNum and not (x,y) in visited):
                return True

    def floodFillDel(self, x, y, visited): #UNUSED
        newVis = visited.copy()
        newVis.append((x,y))
        if (x+1 < constants.GRIDSIZE and self.checkPoint(x + 1, y, self.grid[x][y].colorNum, visited)):
            self.floodFillDel(x+1,y,newVis)
        if (x-1 >= 0 and self.checkPoint(x-1,y,self.grid[x][y].colorNum,visited)):
            self.floodFillDel(x-1,y,newVis)
        if (y+1 < constants.GRIDSIZE and self.checkPoint(x, y + 1, self.grid[x][y].colorNum, visited)):
            self.floodFillDel(x,y+1,newVis)
        if (y-1 >= 0 and self.checkPoint(x,y-1,self.grid[x][y].colorNum,visited)):
            self.floodFillDel(x,y-1,newVis)
        self.grid[x][y]=-1

    def moveCandy(self, x, y, newX, newY):
        self.grid[x][y].updatePos(newX, newY)
        self.grid[newX][newY]=self.grid[x][y]
        self.grid[x][y]=-1

    def checkSwap(self, x1, y1, x2, y2): #FIX ME!
        if (self.grid[x1][y1]!=-1 and self.grid[x2][y2]!=-1):
            col1 = self.grid[x1][y1].colorNum
            col2 = self.grid[x2][y2].colorNum
            testRight1 = True
            testLeft1 = True
            testDown1 = True
            testUp1 = True
            testRight2 = True
            testLeft2 = True
            testDown2 = True
            testUp2 = True
            for i in range(1, constants.INROW):
                if (x2+i < constants.GRIDSIZE):
                    if (self.grid[x2+i][y2]!=-1):
                        if (self.grid[x2+i][y2].colorNum != col1):
                            testRight1 = False
                    else:
                        testRight1 = False
                else:
                    testRight1 = False

                if (x2-i >= 0):
                    if (self.grid[x2-i][y2]!=-1):
                        if (self.grid[x2-i][y2].colorNum != col1):
                            testLeft1 = False
                    else:
                        testLeft1 = False
                else:
                    testLeft1 = False

                if (y2+i < constants.GRIDSIZE):
                    if (self.grid[x2][y2+i]!=-1):
                        if (self.grid[x2][y2+i].colorNum != col1):
                            testDown1 = False
                    else:
                        testDown1 = False
                else:
                    testDown1 = False

                if (y2-i >= 0):
                    if (self.grid[x2][y2-i]!=-1):
                        if (self.grid[x2][y2-i].colorNum != col1):
                            testUp1 = False
                    else:
                        testUp1 = False
                else:
                    testUp1 = False

                if (x1+i < constants.GRIDSIZE):
                    if (self.grid[x1+i][y1]!=-1):
                        if (self.grid[x1+i][y1].colorNum != col2):
                            testRight2 = False
                    else:
                        testRight2 = False
                else:
                    testRight2 = False

                if (x1-i >= 0):
                    if (self.grid[x1-i][y1]!=-1):
                        if (self.grid[x1-i][y1].colorNum != col2):
                            testLeft2 = False
                    else:
                        testLeft2 = False
                else:
                    testLeft2 = False

                if (y1+i < constants.GRIDSIZE):
                    if (self.grid[x1][y1+i]!=-1):
                        if (self.grid[x1][y1+i].colorNum != col2):
                            testDown2 = False
                    else:
                        testDown2 = False
                else:
                    testDown2 = False

                if (y1-i >= 0):
                    if (self.grid[x1][y1-i]!=-1):
                        if (self.grid[x1][y1-i].colorNum != col2):
                            testUp2 = False
                    else:
                        testUp2 = False
                else:
                    testUp2 = False

            return (testRight1 or testLeft1 or testDown1 or testUp1 or testRight2 or testLeft2 or testDown2 or testUp2)
        else:
            return False

    def areMoves(self):
        for y in range(constants.GRIDSIZE - 1):
            for x in range(constants.GRIDSIZE - 1):
                print(str((x,y)) + str(self.checkSwap(x, y, x+1, y)))
                if (self.checkSwap(x, y, x+1, y)):
                    return True

    def clearLines(self):

        planetsToClear = []

        for x in range(constants.GRIDSIZE):
            colNum = 0
            count = 0
            for y in range(constants.GRIDSIZE):
                if (self.grid[x][y]!=-1):
                    if (self.grid[x][y].colorNum==colNum):
                        count+=1
                    else:
                        if (count>=constants.INROW):
                            for i in range(count):
                                planetsToClear.append( (x, y-(i+1)) )
                                #self.grid[x][y-(i+1)]=-1

                        colNum = self.grid[x][y].colorNum
                        count=1
                else:
                    count=0
            if (count>=constants.INROW):
                for i in range(count):
                    planetsToClear.append((x, constants.GRIDSIZE - (i + 1)))
                    #self.grid[x][constants.GRIDSIZE-(i+1)]=-1
        
        for y in range(constants.GRIDSIZE):
            colNum = 0
            count = 0
            for x in range(constants.GRIDSIZE):
                if (self.grid[x][y]!=-1):
                    if (self.grid[x][y].colorNum==colNum):
                        count+=1
                    else:
                        if (count>=constants.INROW):
                            for i in range(count):
                                planetsToClear.append( (x-(i+1), y) )
                                #self.grid[x-(i+1)][y]=-1

                        colNum = self.grid[x][y].colorNum
                        count=1
                else:
                    count=0

            if (count>=constants.INROW):
                for i in range(count):
                    planetsToClear.append((constants.GRIDSIZE - (i + 1), y))
                    #self.grid[constants.GRIDSIZE-(i+1)][y]=-1
        
        for planets in planetsToClear:
            self.grid[planets[0]][planets[1]] = -1
            self.scoreBoard.score += 10
            self.scoreBoard.updateHiScore()
        return planetsToClear

    def doGravity(self):
        move=False
        for fakeY in range(constants.GRIDSIZE - 1):
            y = constants.GRIDSIZE - fakeY - 2
            for x in range(constants.GRIDSIZE):
                if (self.grid[x][y]!=-1):
                    if (self.grid[x][y+1]==-1 or self.grid[x][y+1].isFalling):
                        move=True
                        self.grid[x][y].isFalling = True
                        self.grid[x][y].yGap += constants.FALLSPEED*self.grid[x][y].accel
                        self.grid[x][y].accel*=constants.ACCELERATION
                        if (self.grid[x][y].yGap>constants.CELLSIZE):
                            self.grid[x][y].yGap=0
                            self.grid[x][y].isFalling = False
                            self.moveCandy(x,y,x,y+1)
                    else:
                        self.grid[x][y].accel = 1
                        self.grid[x][y].isFalling = False
        return move


    def addToTop(self):
        for x in range(constants.GRIDSIZE):
            if (self.grid[x][0]==-1):
                self.grid[x][0] = JewelPiece(x, 0, random.randint(0, len(constants.TEXTURES)-1))

    def update(self):
        self.updateSwap()
        hasMoved = self.doGravity()
        if (not hasMoved):
            self.clearLines()
        self.addToTop()
        #print(str(self.areMoves()))

    def startSwap(self, x1, y1, x2, y2, isHor): #Bigins swap
        self.swap1 = self.grid[x1][y1]
        self.swap2 = self.grid[x2][y2]
        self.isHor = isHor
    
    def updateSwap(self): #Animates swap
        if (self.swap1!=-1):
            if (self.isHor):
                self.swap1.xGap += constants.MOVESPEED
                self.swap2.xGap -= constants.MOVESPEED
            else:
                self.swap1.yGap += constants.MOVESPEED
                self.swap2.yGap -= constants.MOVESPEED

            if (self.swap1.xGap>constants.CELLSIZE or self.swap1.yGap>constants.CELLSIZE):
                x1 = self.swap1.x
                y1 = self.swap1.y
                x2 = self.swap2.x
                y2 = self.swap2.y

                self.swap1.updatePos(x2,y2)
                self.swap2.updatePos(x1,y1)
                self.swap1.xGap = 0
                self.swap2.xGap = 0
                self.swap1.yGap = 0
                self.swap2.yGap = 0

                tmp = self.grid[x1][y1]
                self.grid[x1][y1] = self.grid[x2][y2]
                self.grid[x2][y2] = tmp
                self.swap1=-1
                self.swap2=-1
                cleared = self.clearLines()
                if not (self.isSwapBack):
                    if not ((x1, y1) in cleared or (x2, y2) in cleared):
                        self.isSwapBack = True
                        self.startSwap(x1, y1, x2, y2, self.isHor)
                else:
                    self.isSwapBack = False

    def draw(self, screen):
        #Draw Lines
        for x in range(constants.GRIDSIZE):
            if (x!=0):
                pygame.draw.line(screen, constants.LINECOLOR, (x * constants.CELLSIZE, 0), (x * constants.CELLSIZE, constants.SCREENSIZE), int(constants.LINESIZE*constants.CELLSIZE))
                pygame.draw.line(screen, constants.LINECOLOR, (0, x * constants.CELLSIZE), (constants.SCREENSIZE, x * constants.CELLSIZE), int(constants.LINESIZE*constants.CELLSIZE))

        #Draw Planets
        for x in range(constants.GRIDSIZE):
            for y in range(constants.GRIDSIZE):
                if (self.grid[x][y]!=-1):
                     self.grid[x][y].draw(screen)
