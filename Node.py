import math
import constants



class Node():

    weight = 1

    def __init__(self, idx: tuple, endidx: tuple, prt, valAtIdx, isUniformCost=False):
        self.location = idx
        self.endidx = endidx
        self.parent = prt
        self.valAtIdx = valAtIdx

        if prt == None:
            self.distanceFromStartToCurrent = 0
        else:
            self.distanceFromStartToCurrent = prt.distanceFromStartToCurrent + self.calculateDistanceFromParentToCurrent()

        # when weight is one we're performing a unweighted search, when weight > 1 we are performing a weighted search
        if not isUniformCost:
            self.sumOfHeuristicAndDistanceFromStartToCurrent = self.distanceFromStartToCurrent + self.weight * self.calculateEuclideanHeuristic(self.endidx)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.location == other.location

        return False


    def calculateDistanceFromParentToCurrent(self):

        transition = str(self.parent.valAtIdx) + str(self.valAtIdx)
        direction = None

        # For Unweighted search
        if abs(self.parent.location[0] - self.location[0]) == 1 and abs(self.parent.location[1] - self.location[1]) == 1:
            direction = 1
        elif abs(self.parent.location[0] - self.location[0]) == 1 or abs(self.parent.location[1] - self.location[1]) == 1:
            direction = 0

        return self.getTransitionCost(transition, direction)

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
        return math.floor(math.sqrt((endRow - currentRow)**2 + (endColumn - currentColumn)**2))/4

    # Using Manhattan Distance Heuristic
    def calculateManhattanHeuristic(self, endidx: tuple):

        currentRow = self.location[0]
        currentColumn = self.location[1]

        endRow = endidx[0]
        endColumn = endidx[1]

        # using the Manhattan distance formula to calculate heuristic
        return abs(endRow - currentRow) + abs(endColumn - currentColumn)

    # Filters by bounds, checks if not in closed list, and if in open list, sets
    def FilterAndTurnIntoNode(self, expansion: list, open: dict, closed: dict, mapToSearch):

        # Remove Blocked values
        expansion = [Node(idx, self.endidx, self, mapToSearch[idx[0]][idx[1]]) for idx in expansion if idx[0] >= 0 and idx[0] < 120 and idx[1] >= 0 and idx[1] < 160 and mapToSearch[idx[0]][idx[1]] != 0]

        expansion = [node for node in expansion if node.location not in closed]

        for node in expansion:
            if node.location in open:
                if node.sumOfHeuristicAndDistanceFromStartToCurrent < open[node.location].sumOfHeuristicAndDistanceFromStartToCurrent:
                    open[node.location].sumOfHeuristicAndDistanceFromStartToCurrent = node.sumOfHeuristicAndDistanceFromStartToCurrent
                expansion.remove(node)

        return expansion

    def expandNode(self, open, closed, mapToSearch):

        currentRow = self.location[0]
        currentColumn = self.location[1]

        # This expansion definitely can be condensed
        expansion = [(currentRow - 1, currentColumn), (currentRow + 1, currentColumn), (currentRow, currentColumn - 1), (currentRow, currentColumn + 1),
                (currentRow - 1, currentColumn - 1), (currentRow - 1, currentColumn + 1), (currentRow + 1, currentColumn + 1), (currentRow + 1, currentColumn - 1)]

        return self.FilterAndTurnIntoNode(expansion, open, closed, mapToSearch)





class UniformCostNode(Node):

    def __init__(self, idx: tuple, endidx: tuple, prt, isUniformCost=True):
        super().__init__(idx, endidx, prt, isUniformCost)

        # Filters by bounds, checks if not in closed list, and if in open list, sets

    def FilterAndTurnIntoNode(self, expansion: list, open: dict, closed: dict, mapToSearch):

        # Remove Blocked values
        expansion = [UniformCostNode(idx, self.endidx, self, mapToSearch[idx[0]][idx[1]]) for idx in expansion if idx[0] >= 0 and idx[0] < 120 and idx[1] >= 0 and idx[1] < 160]
        expansion = [node for node in expansion if mapToSearch[node.location[0]][node.location[1]] != 0]

        expansion = [node for node in expansion if node.location not in closed]

        for node in expansion:
            if node.location in open:
                if node.distanceFromStartToCurrent < open[node.location].distanceFromStartToCurrent:
                    open[node.location].distanceFromStartToCurrent = node.distanceFromStartToCurrent
                expansion.remove(node)

        return expansion





