import math
import constants



class Node():

    def __init__(self, idx: tuple, endidx: tuple, prt):
        # Current location as a tuple
        self.location = idx

        # Parent that we took to arrive at current location
        self.parent = prt

        # g(n) value
        if prt == None:
            self.distanceFromStartToCurrent = 0
        else:
            self.distanceFromStartToCurrent = prt.distanceFromStartToParent

        #f(n) value = g(n) + h(n) where h(n) is the heuristic
        self.sumOfHeuristicAndDistanceFromStartToCurrent = self.distanceFromStartToCurrent + self.calculateHeuristic(endidx)



    def calculateHeuristic(self, endidx: tuple):

        currentRow = self.location[0]
        currentColumn = self.location[1]

        endRow = endidx[0]
        endColumn = endidx[1]

        # using the distance formula to calculate the heuristic then taking the floor; idk if we want to floor it or just simply compare the float vals
        return math.floor(math.sqrt((endRow - currentRow)**2 + (endColumn - currentColumn)**2))

    def expandNode(self):
        currentRow = self.location[0]
        currentColumn = self.location[1]

        # This expansion definitely can be condensed
        return [(currentRow - 1, currentColumn), (currentRow + 1, currentColumn), (currentRow, currentColumn - 1), (currentRow, currentColumn + 1),
                (currentRow - 1, currentColumn - 1), (currentRow - 1, currentColumn + 1), (currentRow + 1, currentColumn + 1), (currentRow + 1, currentColumn - 1)]








def UnweightedAstarSearch(startidx, endidx):

    selectedNode = Node(startidx, endidx, None)

    print(selectedNode.location)
    print(selectedNode.distanceFromStartToCurrent)
    print(selectedNode.sumOfHeuristicAndDistanceFromStartToCurrent)



if __name__ == "__main__":
    UnweightedAstarSearch((0,0), (119,159))