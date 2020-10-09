import math
import constants



class Node():

    def __init__(self, idx: tuple, endidx: tuple, prt):
        # Current location as a tuple
        self.location = idx
        self.endidx = endidx
        # Parent that we took to arrive at current location
        self.parent = prt

        # g(n) value
        if prt == None:
            self.distanceFromStartToCurrent = 0
        else:
            self.distanceFromStartToCurrent = prt.distanceFromStartToCurrent + self.calculateDistanceFromParentToCurrent()

        #f(n) value = g(n) + h(n) where h(n) is the heuristic
        self.sumOfHeuristicAndDistanceFromStartToCurrent = self.distanceFromStartToCurrent + self.calculateHeuristic(endidx)

    # TODO: Need to modify this code for a weighted search
    def calculateDistanceFromParentToCurrent(self):
        # For Unweighted search
        if abs(self.parent.location[0] - self.location[0]) == 1 and abs(self.parent.location[1] - self.location[1]) == 1:
            return math.sqrt(2)
        elif abs(self.parent.location[0] - self.location[0]) == 1 or abs(self.parent.location[1] - self.location[1]) == 1:
            return 1


    def calculateHeuristic(self, endidx: tuple):

        currentRow = self.location[0]
        currentColumn = self.location[1]

        endRow = endidx[0]
        endColumn = endidx[1]

        # using the distance formula to calculate the heuristic then taking the floor; idk if we want to floor it or just simply compare the float vals
        return math.floor(math.sqrt((endRow - currentRow)**2 + (endColumn - currentColumn)**2))

    def expandNode(self):

        def checkIfInBoundsAndTurnIntoNode(expansion: list):

            expansion = [Node(idx, self.endidx, self) for idx in expansion if idx[0] >= 0 and idx[0] < 120 and idx[1] >= 0 and idx[1] < 160]



            return expansion

        currentRow = self.location[0]
        currentColumn = self.location[1]


        # This expansion definitely can be condensed
        expansion = [(currentRow - 1, currentColumn), (currentRow + 1, currentColumn), (currentRow, currentColumn - 1), (currentRow, currentColumn + 1),
                (currentRow - 1, currentColumn - 1), (currentRow - 1, currentColumn + 1), (currentRow + 1, currentColumn + 1), (currentRow + 1, currentColumn - 1)]

        return checkIfInBoundsAndTurnIntoNode(expansion)








# TODO: Need to modify this code for weighted search
def UnweightedAstarSearch(startidx, endidx):

    # Selected Node will be initialized to the start node
    selectedNode = Node(startidx, endidx, None)

    open = []
    closed = []

    # initial expansion of the start node
    open.extend(selectedNode.expandNode())
    closed.append(selectedNode)

    # TODO: BELOW NEEDS TO BE MODIFIED SINCE SELECTED NODES WILL EXPAND AND APPEND TO OPEN NODES THAT ARE IN CLOSED SET 
    while selectedNode.location != endidx:

        for node in open:
            if node.sumOfHeuristicAndDistanceFromStartToCurrent < selectedNode.sumOfHeuristicAndDistanceFromStartToCurrent:
                selectedNode = node

        # remove the selected node from the open list then append to the closed list
        closed.append(open.remove(selectedNode))

        open.extend(selectedNode.expandNode())













if __name__ == "__main__":
    UnweightedAstarSearch((0,0), (119,159))