
#May want to use these
import pandas
import numpy as np
import random



# May want to make this into a class or just a list of methods (idk which would be better)
class MapData():


    def __init__(self):
        #object lvl fields can be initialized in here
        self.map = None


    def createDefaultMap(self):
        self.map = np.ones((160, 120))

    def generatingBlockedCells(self):

        for i in range(0,8):
            x, y = random.randint(0,120), random.randint(0,160)

            for i in range(x, x + 31):
                if i >= 160:
                    break
                for j in range(y, y + 31):
                    if y >= 120:
                      break

                    self.map[x,y] = random.choice([0, 1])













if __name__ == "__main__":
    testMap = MapData()
    testMap.createDefaultMap()
    testMap.generatingBlockedCells()







