
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
        # self.generateBoostCells()
        # self.generateBlockedCells()

    def createDefaultMap(self):
        self.map = np.ones((constants.NUMBER_OF_BLOCKS_HIGH, constants.NUMBER_OF_BLOCKS_WIDE))

    def generatingHardToTraverseCells(self):

        for i in range(0,8):
            x, y = random.randint(0,120), random.randint(0,160)
            print(x, y)
            for i in range(x, x + 31):
                if i >= 120:
                    break
                for j in range(y, y + 31):
                    if j < 160:
                        self.map[i, j] = random.choice([0, 1])
                    else:
                        break


    def generateBoostCells(self):
        selections = {"R1": 0, "C1": 0, "R2": 120, "C2": 160}
        sideSelection = random.choices(list(selections.keys()))[0]

        self.generateBoostCellsInitialStep(sideSelection, selections)


    def generateBoostCellsInitialStep(self, sideSelection, selections):

        row, column = None, None
        if(sideSelection == "R1" or sideSelection == "R2"):
            row, column = (selections[sideSelection], random.randint(0, 160))
        elif(sideSelection == "C1" or sideSelection == "C2"):
            row, column = (random.randint(0,120), selections[sideSelection])


        if(sideSelection == "R1"):
            for x in range(row, row + 20):
                if self.map[x, column] == 1:
                    self.map[x, column] = 'a'
                elif self.map[x, column] == 2:
                    self.map[x, column] = 'b'

        elif (sideSelection == "R2"):
            for x in range(row, row - 20, -1):
                if self.map[x, column] == 1:
                    self.map[x, column] = 'a'
                elif self.map[x, column] == 2:
                    self.map[x, column] = 'b'
        elif(sideSelection == "C1"):
            for y in range(column, column + 20):
                if self.map[row, y] == 1:
                    self.map[row, y] = 'a'
                elif self.map[row, y] == 2:
                    self.map[row, y] = 'b'
        elif(sideSelection == "C2"):
            for y in range(column, column - 20, -1):
                if self.map[row, y] == 1:
                    self.map[row, y] = 'a'
                elif self.map[row, y] == 2:
                    self.map[row, y] = 'b'




    def generateBlockedCells(self):
        pass














if __name__ == "__main__":
    testMap = MapData()
    testMap.createDefaultMap()
    testMap.generatingHardToTraverseCells()
    testMap.generateBoostCells()




