import math
import constants



class Node():

    weight = 1

    def __init__(self, idx: tuple, endidx: tuple, prt):
        # Current location as a tuple
        self.location = idx
        self.endidx = endidx
        # Parent that we took to arrive at current location
        self.parent = prt
        if prt == None:
            self.distanceFromStartToCurrent = 0
        else:
            self.distanceFromStartToCurrent = prt.distanceFromStartToCurrent + self.calculateDistanceFromParentToCurrent()

        # when weight is one we're performing a unweighted search, when weight > 1 we are performing a weighted search
        self.sumOfHeuristicAndDistanceFromStartToCurrent = self.distanceFromStartToCurrent + self.weight * self.calculateEuclideanHeuristic(self.endidx)


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

    # transition is combined string of values of the two squares we are currently looking at
    # direction is 0 for vertical/horizontal and 1 for diagonal
    def getTransitionCost(self, transition, direction):
        if transition == '11' or transition == 'a1' or transition == '1a':
            if direction == 0:
                return 1
            if direction == 1:
                return math.sqrt(2)
        elif transition == '22' or transition == 'b2' or transition == '2b':
            if direction == 0:
                return 2
            if direction == 1:
                return math.sqrt(8)
        elif transition == '21' or transition == '12' or transition == 'b1' or transition == '1b' or transition == 'a2' or transition == '2a':
            if direction == 0:
                return 1.5
            if direction == 1:
                return math.sqrt(2) * 3 / 2
        elif transition == 'ab' or transition == 'ba':
            return .375
        elif transition == 'aa':
            return .25
        elif transition == 'bb':
            return .5


    # Using Euclidean Distance
    def calculateEuclideanHeuristic(self, endidx: tuple):

        currentRow = self.location[0]
        currentColumn = self.location[1]

        endRow = endidx[0]
        endColumn = endidx[1]

        # using the distance formula to calculate the heuristic then taking the floor; idk if we want to floor it or just simply compare the float vals
        return math.floor(math.sqrt((endRow - currentRow)**2 + (endColumn - currentColumn)**2))

    # Using Manhattan Distance Heuristic
    def calculateManhattanHeuristic(self, endidx: tuple):

        currentRow = self.location[0]
        currentColumn = self.location[1]

        endRow = endidx[0]
        endColumn = endidx[1]

        # using the Manhattan distance formula to calculate heuristic
        return math.fabs(endRow - currentRow) + math.fabs(endColumn - currentColumn)


    def expandNode(self, open, closed, map):

        # Filters by bounds, checks if not in closed list, and if in open list, sets
        def FilterAndTurnIntoNode(expansion: list, open: dict, closed: dict):

            # Remove Blocked values
            expansion = [Node(idx, self.endidx, self) for idx in expansion if idx[0] >= 0 and idx[0] < 120 and idx[1] >= 0 and idx[1] < 160]
            expansion = [node for node in expansion if map[node.location[0]][node.location[1]] != 0]

            expansion = [node for node in expansion if node.location not in closed]

            for node in expansion:
                if node.location in open:
                    if node.sumOfHeuristicAndDistanceFromStartToCurrent < open[node.location].sumOfHeuristicAndDistanceFromStartToCurrent:
                            open[node.location].sumOfHeuristicAndDistanceFromStartToCurrent = node.sumOfHeuristicAndDistanceFromStartToCurrent
                    expansion.remove(node)


            return expansion


        currentRow = self.location[0]
        currentColumn = self.location[1]


        # This expansion definitely can be condensed
        expansion = [(currentRow - 1, currentColumn), (currentRow + 1, currentColumn), (currentRow, currentColumn - 1), (currentRow, currentColumn + 1),
                (currentRow - 1, currentColumn - 1), (currentRow - 1, currentColumn + 1), (currentRow + 1, currentColumn + 1), (currentRow + 1, currentColumn - 1)]

        return FilterAndTurnIntoNode(expansion, open, closed)





class UniformCostNode(Node):

    def __init__(self):
        pass




