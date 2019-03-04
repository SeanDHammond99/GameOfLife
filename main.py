import time
from random import *
import os
class Grid(object):
    def __init__(self, size):
        self.grid=[]
        self.size=size
        for i in range(size):
            line=[]
            for j in range(size):
                line.append(" ")
            self.grid.append(line)

    def print(self):
        os.system("cls")
        for line in  range(len(self.grid)):
            stringline=""
            for ele in self.grid[line]:
                stringline+=ele
            print(stringline)

    def checkCell(self,x,y):
        return self.grid[y][x]

    def setCell(self, x, y, value="#"):
        self.grid[y][x]=value

    def checkNeighbour(self,x,y):
        neighbours=0
        for i in [x-1,x,x+1]:
            if i == self.size:
                i = 0
            if i <0:
                i=self.size-1
            if i in range(0,self.size):
                for j in [y-1,y,y+1]:
                    if j == self.size:
                        j = 0
                    if j <0:
                        j=self.size-1
                    if j in range(0,self.size):
                        if self.checkCell(i,j)=="#" and (x,y) != (i,j):
                            neighbours+=1

        return neighbours

    def nextValue(self, x, y):
        current_value = self.checkCell(x, y)
        neighbours = [" "," ",current_value, "#", " "," "," "," "," "]
        return neighbours[self.checkNeighbour(x, y)]

    def tickGrid(self):
        new_grid = Grid(self.size)
        for row in range(len(self.grid)):
            for column in range(len(self.grid)):
                new_grid.grid[row][column] = self.nextValue(column, row)
        self.grid = new_grid.grid
        return new_grid

    def randomStart(self):
        for row in range(len(self.grid)):
            for column in range(len(self.grid)):
                self.grid[row][column] = [" ","#"][randint(0,1)]
            
                

