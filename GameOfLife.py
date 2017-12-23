## Importing Modules
import time
import math
import random
from graphics import *

class cell:

    def __init__(self,active,save,x,y):
        ## Save state intially stores the change so that the change doesn't affect the check for the other cells
        self.active = bool(active)
        self.save = bool(save)
        self.x = int(x)
        self.y = int(y)

    def life(self):
        self.save = True
            
    def death(self):
        self.save = False

    def switch(self):
        ## Changes the save and active state when the checking is finished
        self.active = self.save
        self.save = False

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getState(self):
        return self.active

    def getSave(self):
        return self.save

    def dlife(self):
        ## Directly changes the value for user input
        self.active = True

    def ddeath(self):
        ## Directly changes the value for user input
        self.active = False

def makecoor(x,y):
    ## Makes all the cells
    cells = []
    for i in range(x):
        ## Turns the array 2D
        cells.append([])
    for i in range(x):
        for k in range(y):
            ## Fills the array
            cells[i].append(cell(False,False,i,k))
    return cells

def cellcheck(cells,i,k,j,p,count):
    ## Checks if the nieghbouring cells are alive
    if (cells[i+j][k+p].getState() == True) and (j != 0 or p != 0):
        count += 1
    return count
    
def update(cells,grid):
    ## Array used to access the nieghbouring cells
    neigh = [-1,0,1]
    ## Does the update for all cells
    for i in range(len(cells)):
        for k in range(len(cells[i])):
            count = 0
            ## Counts the cells neighbouring
            for j in neigh:
                if ((j+i) >= len(cells)):
                    j = (len(cells)-1)*-1
                for p in neigh:
                    if ((k+p) >= len(cells[i])):
                        p = (len(cells[i])-1)*-1
                    count = cellcheck(cells,i,k,j,p,count)
            ## Game of life algorithm
            if (cells[i][k].getState() == True):
                if count < 2:
                    cells[i][k].death()
                    grid[i][k].setFill("white")
                elif count > 3:
                    cells[i][k].death()
                    grid[i][k].setFill("white")
                else:
                    cells[i][k].life()
                    ##grid[i][k].setFill("black") (its already black)
            elif (cells[i][k].getState() == False):
                if count == 3:
                    cells[i][k].life()
                    grid[i][k].setFill("black")
                else:
                    cells[i][k].death()
                    ##grid[i][k].setFill("white") (its already white)
    ## Switches the save and active states
    for i in range(len(cells)):
        for k in range(len(cells[i])):
            cells[i][k].switch()

def gridsetup(win,x,y):
    ## Sets up the visuals
    grid = []
    ## Creates 2D aarray of squares from the Graphics Module
    for i in range(x):
        tgrid = []
        for k in range(y):
            tgrid = tgrid + [Rectangle(Point(i, k), Point(i+1, k+1))]
        grid = grid + [tgrid]
    for i in range(x):
        for k in range(y):
            ## Makes all the squares white
            grid[i][k].setOutline("white")
            grid[i][k].setFill("white")
            grid[i][k].draw(win)
    return grid

def draw(cells,grid,win):
    ## Updates the visuals
    for i in range(len(cells)):
        for k in range(len(cells[i])):
            if (cells[k][i].getState() == False):
                grid[i][k].setFill("white")
            elif (cells[k][i].getState() == True):
                grid[i][k].setFill("black")

def live(cells,grid,x,y):
    ## For user input
    cells[x][y].dlife()
    grid[x][y].setFill("black")

def die(cells,grid,x,y):
    ## For user input
    cells[x][y].ddeath()
    grid[x][y].setFill("white")

def mouse(win,cells,grid):
    ## Mouse input using the Graphics Module's getMouse class
    p = ""
    for i in range(10):
        p = win.getMouse()
        live(cells,grid,int(math.floor(p.getX())),int(math.floor(p.getY())))

def glider(cells,grid):
    ## For testing
    live(cells,grid,2,1)
    live(cells,grid,3,2)
    live(cells,grid,3,3)
    live(cells,grid,2,3)
    live(cells,grid,1,3)
        
def main():
    x = 25
    y = 25
    cells = makecoor(x,y)

    win = GraphWin("Game of Life", 500, 600)
    win.setCoords(0,x+5,y,0)
    win.setBackground("white")
    grid = gridsetup(win,x,y)

    ## Graphics UI
    t1 = Text(Point(12,26),"Instructions")
    t1.draw(win)
    t2 = Text(Point(12,28),"Press 'q' to quit     Press 's' to step forward\nPress 'c' to step 25 steps     \
Press 'r' to fill randomly\nPress 'k' to fill with mouse 10 times     Press 'p' to clear")
    t2.draw(win)

    live(cells,grid,10,9)
    live(cells,grid,10,8)
    live(cells,grid,10,7)
    glider(cells,grid)

    key = ""

    ## Menu
    while (key != "q" or key != "Q"):
        key = win.getKey()
        if (key == "s" or key == "S"):
            update(cells,grid)
            ##draw(cells,grid,win)
        if (key == "k" or key == "K"):
            mouse(win,cells,grid)
        if (key == "c" or key == "C"):
            for i in range(25):
                update(cells,grid)
                ##draw(cells,grid,win)
                time.sleep(0.2)
        if (key == "r" or key == "R"):
            for i in range(random.randrange(0,125)):
                live(cells,grid,random.randrange(1,x),random.randrange(1,y))
            for i in range(random.randrange(0,125)):
                die(cells,grid,random.randrange(1,x),random.randrange(1,y))
        if (key == "p" or key == "P"):
            for i in range(25):
                for k in range(25):
                    die(cells,grid,i,k)
        if (key == "q" or key == "Q"):
            break

    win.close()
    
if __name__ == '__main__':
    main()

##def textprint(cells):
#### User for testing
##    output = ''
##    for i in range(len(cells)):
##        for k in range(len(cells[i])):
##            if (cells[k][i].getState() == False):
##                output += " o"
##            elif (cells[k][i].getState() == True):
##                output += " +"
##        output += "\n"
##    return output

