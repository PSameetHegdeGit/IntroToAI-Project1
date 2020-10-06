
#May want to use pandas dataframe instead of a numpy array
import pandas
import numpy as np
import random
import constants





# May want to make this into a class or just a list of methods (idk which would be better)
class MapData():


    def __init__(self):
        #object lvl fields can be initialized in here
        self.map = None



    def runSuite(self):
        self.createDefaultMap()
        self.generatingHardToTraverseCells()
        self.generateBoostCells()
        # self.generateBlockedCells()

    def createDefaultMap(self):
        self.map = np.ones((constants.NUMBER_OF_BLOCKS_HIGH, constants.NUMBER_OF_BLOCKS_WIDE))

    def generatingHardToTraverseCells(self):

        for i in range(0,8):
            x, y = random.randint(0,119), random.randint(0,159)
            for i in range(x, x + 31):
                if i >= 120:
                    break
                for j in range(y, y + 31):
                    if j < 160:
                        self.map[i, j] = random.choice([1,2])
                    else:
                        break


    # Noticed bug where path does not extend 20 cells for a single translation
    def generateBoostCells(self):
        selections = {"R1": 0, "C1": 0, "R2": 119, "C2": 159}
        sideSelection = random.choices(list(selections.keys()))[0]

        newrow, newcolumn = self.generateBoostCellsInitialStep(sideSelection, selections)
        self.generateBoostCellsLaterSteps(newrow, newcolumn, sideSelection)


    #TODO: Convert numpy array back to regular 2D array;
    def generateBoostCellsInitialStep(self, sideSelection, selections):

        row, column = None, None
        if(sideSelection == "R1" or sideSelection == "R2"):
            row, column = (selections[sideSelection], random.randint(0, 159))
        elif(sideSelection == "C1" or sideSelection == "C2"):
            row, column = (random.randint(0,119), selections[sideSelection])


        if(sideSelection == "R1"):
            for x in range(row, row + 20):
                if self.map[x, column] == 1:
                    self.map[x, column] = 3
                elif self.map[x, column] == 2:
                    self.map[x, column] = 4

                row = x

        elif (sideSelection == "R2"):
            for x in range(row, row - 20, -1):
                if self.map[x, column] == 1:
                    self.map[x, column] = 3
                elif self.map[x, column] == 2:
                    self.map[x, column] = 4

                row = x
        elif(sideSelection == "C1"):
            for y in range(column, column + 20):
                if self.map[row, y] == 1:
                    self.map[row, y] = 3
                elif self.map[row, y] == 2:
                    self.map[row, y] = 4

                column = y
        elif(sideSelection == "C2"):
            for y in range(column, column - 20, -1):
                if self.map[row, y] == 1:
                    self.map[row, y] = 3
                elif self.map[row, y] == 2:
                    self.map[row, y] = 4

                column = y


        return row, column

    def generateBoostCellsLaterSteps(self, row, column, sideSelection):

        sideSelectionToRoute = {"R1": "Down", "R2": "Up", "C1": "Right", "C2": "Left"}
        sameRoute = sideSelectionToRoute[sideSelection]


        routeToPerpendicularPaths = {"Up": ["Left", "Right"], "Down": ["Left", "Right"], "Left": ["Up", "Down"], "Right": ["Up", "Down"]}
        print(sameRoute)

        while row >= 0 and row < 120 and column >= 0 and column < 160:
            choice = random.choices(["Same", "Perpendicular"], [0.6, 0.2])[0]

            if choice == "Same":
                print(sameRoute)
                row, column = self.tryTranslating20Cells(sameRoute, row, column)

            elif choice == "Perpendicular":
                # Choose with equal probability
                route = random.choices(routeToPerpendicularPaths[sameRoute])[0]
                print(route)
                row, column = self.tryTranslating20Cells(route, row, column)

                sameRoute = route





    # Given a particular direction move by 20
    def tryTranslating20Cells(self, route, row, column):

        if route == "Up":
            for x in range(row, row - 20, -1):
                if self.map[x, column] == 1:
                    self.map[x, column] = 3
                elif self.map[x, column] == 2:
                    self.map[x, column] = 4

                row = x
        elif route == "Down":
            for x in range(row, row + 20):
                if self.map[x, column] == 1:
                    self.map[x, column] = 3
                elif self.map[x, column] == 2:
                    self.map[x, column] = 4

                row = x
        elif route == "Left":
            for y in range(column, column - 20, -1):
                if self.map[row, y] == 1:
                    self.map[row, y] = 3
                elif self.map[row, y] == 2:
                    self.map[row, y] = 4

                column = y
        elif route == "Right":
            for y in range(column, column + 20):
                if self.map[row, y] == 1:
                    self.map[row, y] = 3
                elif self.map[row, y] == 2:
                    self.map[row, y] = 4

                column = y


        return row, column



    def generateBlockedCells(self):
        pass














if __name__ == "__main__":
    testMap = MapData()
    testMap.createDefaultMap()
    testMap.generatingHardToTraverseCells()
    testMap.generateBoostCells()




