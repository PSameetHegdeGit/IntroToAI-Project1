import math


class Node():



    def __init__(self, idx, endidx, prt, valAtIdx, weight=1, isUniformCost=False, isMultiHeuristic = False):
        self.location = idx
        self.endidx = endidx
        self.parent = prt
        self.valAtIdx = valAtIdx
        self.weight = weight
        self.isUniformCost = isUniformCost
        self.isMultiHeuristic = isMultiHeuristic


        if prt is None:
            self.distanceFromStartToCurrent = 0
        else:
            self.distanceFromStartToCurrent = prt.distanceFromStartToCurrent + self.calculateDistanceFromParentToCurrent()

        if isMultiHeuristic:
            if prt is None:
                self.distanceFromStartToCurrent = [0]*5
                self.bestparent = [None] * 5
            else:
                for i in range(5):
                    self.distanceFromStartToCurrent[i] = prt.distanceFromStartToCurrent[i] + self.calculateDistanceFromParentToCurrent()
                    self.bestparent[i] = prt



        if not isUniformCost:
            self.sumOfHeuristicAndDistanceFromStartToCurrent = self.distanceFromStartToCurrent + self.weight * (self.calculateEuclideanHeuristic(self.endidx))

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.location == other.location

        return False


    def calculateDistanceFromParentToCurrent(self):

        transition = str(self.parent.valAtIdx) + str(self.valAtIdx)
        direction = None

        if abs(self.parent.location[0] - self.location[0]) == 1 and abs(self.parent.location[1] - self.location[1]) == 1:
            direction = 1
        elif abs(self.parent.location[0] - self.location[0]) == 1 or abs(self.parent.location[1] - self.location[1]) == 1:
            direction = 0

        return self.getTransitionCost(transition, direction)


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


    def calculateEuclideanHeuristic(self, endidx: tuple):

        currentRow = self.location[0]
        currentColumn = self.location[1]

        endRow = endidx[0]
        endColumn = endidx[1]

        return math.floor(math.sqrt((endRow - currentRow)**2 + (endColumn - currentColumn)**2))/4

    def calculateManhattanHeuristic(self, endidx: tuple):

        currentRow = self.location[0]
        currentColumn = self.location[1]

        endRow = endidx[0]
        endColumn = endidx[1]

        return abs(endRow - currentRow) + abs(endColumn - currentColumn)

    def calculateChebyshevHeuristic(self, endidx: tuple):
        currentRow = self.location[0]
        currentColumn = self.location[1]

        endRow = endidx[0]
        endColumn = endidx[1]

        return max(abs(endRow - currentRow), abs(endColumn - currentColumn)) / 3

    def calculateOctileHeuristic(self, endidx: tuple):
        currentRow = self.location[0]
        currentColumn = self.location[1]

        endRow = endidx[0]
        endColumn = endidx[1]

        dx = abs(currentRow - endRow)
        dy = abs(currentColumn - endColumn)

        return ((dx + dy) + (math.sqrt(2) - 2) * min(dx, dy))/4

    def calculateBrayCurtisHeuristic(self, endidx: tuple):
        currentRow = self.location[0]
        currentColumn = self.location[1]

        endRow = endidx[0]
        endColumn = endidx[1]

        return "Bray Curtis dist", (abs(endRow - currentRow) + abs(endColumn - currentColumn))/(abs(endRow + currentRow) + abs(endColumn + currentColumn))


    def FilterAndTurnIntoNode(self, expansion: list, open: dict, closed: dict, mapToSearch, minheap):
        """
        filters nodes that are ineligible to be expanded and also filters out nodes in closed
        Also filters out nodes currently in open but updates those nodes if cost is less

        :param expansion: list
        :param open: dict
        :param closed: dict
        :param mapToSearch: [][]
        :param minheap: MinHeap()
        :return: expansion
        """


        expansion = [Node(idx, self.endidx, self, mapToSearch[idx[0]][idx[1]], self.weight, self.isUniformCost, self.isMultiHeuristic) for idx in expansion if idx[0] >= 0 and idx[0] < 120 and idx[1] >= 0 and idx[1] < 160 and mapToSearch[idx[0]][idx[1]] != 0]

        expansion = [node for node in expansion if node.location not in closed]

        expansionToSend = []

        for node in expansion:
            if node.location in open:
                if node.sumOfHeuristicAndDistanceFromStartToCurrent < open[node.location].sumOfHeuristicAndDistanceFromStartToCurrent:
                    open[node.location].sumOfHeuristicAndDistanceFromStartToCurrent = node.sumOfHeuristicAndDistanceFromStartToCurrent
                    open[node.location].parent = node.parent
                    index = minheap.minheap.index(open[node.location])
                    minheap.sift_up(index)
                expansion.remove(node)
            else:
                expansionToSend.append(node)

        return expansion



    def expandNode(self, open, closed, mapToSearch, minheap):
        """
        generates expansion which is a list of the indices accessible from current idx

        :param open: []
        :param closed: []
        :param mapToSearch: [][]
        :param minheap: MinHeap()
        :return: expansion
        """

        currentRow = self.location[0]
        currentColumn = self.location[1]

        # This expansion definitely can be condensed
        expansion = [(currentRow - 1, currentColumn), (currentRow + 1, currentColumn), (currentRow, currentColumn - 1), (currentRow, currentColumn + 1),
                (currentRow - 1, currentColumn - 1), (currentRow - 1, currentColumn + 1), (currentRow + 1, currentColumn + 1), (currentRow + 1, currentColumn - 1)]

        return self.FilterAndTurnIntoNode(expansion, open, closed, mapToSearch, minheap)





class UniformCostNode(Node):
    """
        This class is utilized by Uniform Cost Search.

        child FilterAndTurnIntoNode() checks cost distanceFromStartToCurrent

    """

    def __init__(self, idx, endidx, prt, valAtIdx, isUniformCost=True, isMultiHeuristic=False):
        super().__init__(idx, endidx, prt, valAtIdx, isUniformCost)


    def FilterAndTurnIntoNode(self, expansion: list, open: dict, closed: dict, mapToSearch, minheap):


        expansion = [UniformCostNode(idx, self.endidx, self, mapToSearch[idx[0]][idx[1]], self.isUniformCost) for idx in expansion if idx[0] >= 0 and idx[0] < 120 and idx[1] >= 0 and idx[1] < 160 and mapToSearch[idx[0]][idx[1]] != 0]

        expansion = [node for node in expansion if node.location not in closed]

        expansionToSend = []

        for node in expansion:
            if node.location in open:
                if node.distanceFromStartToCurrent < open[node.location].distanceFromStartToCurrent:
                    open[node.location].distanceFromStartToCurrent = node.distanceFromStartToCurrent
                    open[node.location].parent = node.parent
                    index = minheap.minheap.index(open[node.location])
                    minheap.sift_up(index)
            else:
                expansionToSend.append(node)
        return expansionToSend




