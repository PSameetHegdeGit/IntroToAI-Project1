
#May want to use pandas dataframe instead of a numpy array
import pandas
import numpy as np
import random
import constants
import math
from helper import *


# May want to make this into a class or just a list of methods (idk which would be better)
class MapData():


    def __init__(self):
        #object lvl fields can be initialized in here
        self.map = []
        self.hardToTraverseIndices = []



    def runSuite(self):

        self.createDefaultMap()
        self.generatingHardToTraverseCells()
        for i in range(4):
            self.generateBoostCells()
        self.generateBlockedCells()


    def createDefaultMap(self):
        self.map = [[1 for column in range(constants.NUMBER_OF_BLOCKS_WIDE)]for row in range(constants.NUMBER_OF_BLOCKS_HIGH)]

    def generatingHardToTraverseCells(self):

        for i in range(0,8):
            x, y = random.randint(0,119), random.randint(0,159)
            for i in range(x, x + 31):
                if i >= 120:
                    break
                for j in range(y, y + 31):
                    if j < 160:
                        self.map[i][j] = random.choice([1,2])
                    else:
                        break
            self.hardToTraverseIndices.append((x,y))


    # Noticed bug where path does not extend 20 cells for a single translation
    def generateBoostCells(self):

        selections = {"R1": 0, "C1": 0, "R2": 119, "C2": 159}
        sideSelection = random.choices(list(selections.keys()))[0]
        indicesOfPath = []

        while True:
            try:

                newrow, newcolumn = self.generateBoostCellsInitialStep(sideSelection, selections[sideSelection], indicesOfPath)
                self.generateBoostCellsLaterSteps(newrow, newcolumn, sideSelection, indicesOfPath)

                  # if count is greater than 100 our highway is valid
                if len(indicesOfPath) >= 100:
                    break

            # Raise an exception on collision with an already established path
            except CollisionError:
                pass

            self.resetPathValues(indicesOfPath)
            indicesOfPath.clear()


    # Function resets the values of path back to one
    def resetPathValues(self, indicesOfPath):
        for idx in indicesOfPath:
            self.map[idx[0]][idx[1]] = 1


    def generateBoostCellsInitialStep(self, sideSelection, idxFromSelection, indicesOfPath):

        row, column = None, None
        if sideSelection == "R1" or sideSelection == "R2":
            row, column = (idxFromSelection, random.randint(0, 159))
        elif sideSelection == "C1" or sideSelection == "C2":
            row, column = (random.randint(0,119), idxFromSelection)

        if self.map[row][column] == 'a' or self.map[row][column] == 'b':
            raise CollisionError()

        if self.map[row][column] == 1:
            self.map[row][column] = 'a'
        elif self.map[row][column] == 2:
            self.map[row][column] = 'b'

        indicesOfPath.append((row,column))


        if sideSelection == "R1":
            row, column = Down(self.map, row, column, indicesOfPath)
        elif sideSelection == "R2":
            row, column = Up(self.map, row, column, indicesOfPath)
        elif sideSelection == "C1":
            row, column = Right(self.map, row, column, indicesOfPath)
        elif sideSelection == "C2":
            row, column = Left(self.map, row, column, indicesOfPath)

        return row, column

    def generateBoostCellsLaterSteps(self, row, column, sideSelection, indicesOfPath):

        sideSelectionToRoute = {"R1": "Down", "R2": "Up", "C1": "Right", "C2": "Left"}
        route = sideSelectionToRoute[sideSelection]
        routeToPerpendicularPaths = {"Up": ["Left", "Right"], "Down": ["Left", "Right"], "Left": ["Up", "Down"], "Right": ["Up", "Down"]}

        while row > 0 and row < 119 and column > 0 and column < 159:
            choice = random.choices(["Same", "Perpendicular"], [0.6, 0.4])[0]

            # choice = "Same"

            if choice == "Same":
                row, column = self.translate20Cells(route, row, column, indicesOfPath)


            elif choice == "Perpendicular":
                # Choose with equal probability
                route = random.choices(routeToPerpendicularPaths[route])[0]
                row, column = self.translate20Cells(route, row, column, indicesOfPath)





    # Given a particular direction move by 20 -- NEEDS TO BE MODIFIED
    def translate20Cells(self, route, row, column, indicesOfPath):

        if route == "Up":
            row, column = Up(self.map, row, column, indicesOfPath)
        elif route == "Down":
            row, column = Down(self.map, row, column, indicesOfPath)
        elif route == "Left":
            row, column = Left(self.map, row, column, indicesOfPath)
        elif route == "Right":
            row, column = Right(self.map, row, column, indicesOfPath)

        return row, column




    def generateBlockedCells(self):

        indices = [(row, column) for row in range(len(self.map)) for column in range(len(self.map[0]))]

        for idx in random.choices(indices, k=math.floor(len(indices) * 0.2)):
            if self.map[idx[0]][idx[1]] == 'a' or self.map[idx[0]][idx[1]] == 'b':
                continue
            else:
                self.map[idx[0]][idx[1]] = 0



    def generateTuple(self, region, idx):


        while idx is None or self.map[idx[0]][idx[1]] == 0:
            print(idx)
            if idx is not None:
                print(self.map[idx[0]][idx[1]])
            if region == 'TOP':
                idx = (random.randrange(0,20), random.randrange(0, 160))
            elif region  == 'BOTTOM':
                idx = (random.randrange(99, 120), random.randrange(0, 160))
            elif region == 'LEFT':
                idx = (random.randrange(0, 120), random.randrange(0,20))
            elif region == 'RIGHT':
                idx = (random.randrange(0, 120), random.randrange(139, 160))

        print(idx)
        print(self.map[idx[0]][idx[1]])

        return idx




    def generateStartAndEndIndices(self):


        regions = ['TOP', 'BOTTOM', 'LEFT', 'RIGHT']

        startregion = random.choice(regions)

        regions.remove(startregion)

        endregion = random.choice(regions)

        startidx = self.generateTuple(startregion, None)
        endidx = self.generateTuple(endregion, None)


        return startidx, endidx





if __name__ == "__main__":
    testMap = MapData()
    testMap.runSuite()
    testMap.generateStartAndEndIndices()
    print(testMap.map)




