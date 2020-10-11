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


    def __eq__(self, other):
        if isinstance(other, Node):
            return self.location == other.location

        return False




    # TODO: Need to modify this code for a weighted search
    def calculateDistanceFromParentToCurrent(self):
        # For Unweighted search
        if abs(self.parent.location[0] - self.location[0]) == 1 and abs(self.parent.location[1] - self.location[1]) == 1:
            return math.sqrt(2)
        elif abs(self.parent.location[0] - self.location[0]) == 1 or abs(self.parent.location[1] - self.location[1]) == 1:
            return 1


    # Using Euclidean Distance
    def calculateHeuristic(self, endidx: tuple):

        currentRow = self.location[0]
        currentColumn = self.location[1]

        endRow = endidx[0]
        endColumn = endidx[1]

        # using the distance formula to calculate the heuristic then taking the floor; idk if we want to floor it or just simply compare the float vals
        return math.floor(math.sqrt((endRow - currentRow)**2 + (endColumn - currentColumn)**2))

    def expandNode(self, open, closed):

        # Filters by bounds, checks if not in closed list, and if in open list, sets
        def FilterAndTurnIntoNode(expansion: list, open: list, closed: list):

            expansion = [Node(idx, self.endidx, self) for idx in expansion if idx[0] >= 0 and idx[0] < 120 and idx[1] >= 0 and idx[1] < 160]

            expansion = [node for node in expansion if node not in closed]

            for node in expansion:
                for term in open:
                    if node == term:
                        if node.sumOfHeuristicAndDistanceFromStartToCurrent < term.sumOfHeuristicAndDistanceFromStartToCurrent:
                            term.sumOfHeuristicAndDistanceFromStartToCurrent = node.sumOfHeuristicAndDistanceFromStartToCurrent


            return expansion


        currentRow = self.location[0]
        currentColumn = self.location[1]


        # This expansion definitely can be condensed
        expansion = [(currentRow - 1, currentColumn), (currentRow + 1, currentColumn), (currentRow, currentColumn - 1), (currentRow, currentColumn + 1),
                (currentRow - 1, currentColumn - 1), (currentRow - 1, currentColumn + 1), (currentRow + 1, currentColumn + 1), (currentRow + 1, currentColumn - 1)]

        return FilterAndTurnIntoNode(expansion, open, closed)
