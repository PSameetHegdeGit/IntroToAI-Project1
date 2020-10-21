import heapq
from MinHeap import *
from Node import *



def backtrack(node: Node, startidx: tuple, mapToSearch):

    """
        Prints out indices of optimal path from end back to start and sets those indices to optimal
    """

    if node.location == startidx:
        mapToSearch[node.location[0]][node.location[1]] = 'optimal'
        return node.location
    mapToSearch[node.location[0]][node.location[1]] = 'optimal'
    return f"{node.location} {backtrack(node.parent, startidx, mapToSearch)}"

def backtrackTesting(node: Node, startidx: tuple, mapToSearch):

    """
            Prints out indices of optimal path from end back to start but specifically used for testing
    """

    if node.location == startidx:
        return 1
    return 1 + backtrackTesting(node.parent, startidx, mapToSearch)


def UniformCost(startidx, endidx, mapToSearch):



    try:
        selectedNode = UniformCostNode(startidx, endidx, None, mapToSearch[startidx[0]][startidx[1]])

        open = MinHeapForUniform()

        openIndices = {}
        closed = {}


        while selectedNode.location != endidx:

            expansion = selectedNode.expandNode(openIndices, closed, mapToSearch, open)

            for node in expansion:
                open.insert(node)
                openIndices[node.location] = node

            selectedNode = open.remove()

            try:
                openIndices.pop(selectedNode.location)
            except:
                pass

            if len(openIndices) == 0:
                print("Sorry unreachable!")
                return openIndices, closed

            closed[selectedNode.location] = selectedNode


        print(backtrack(selectedNode, startidx, mapToSearch))
        return openIndices, closed
    except:
        print("Search Failed!")
        return None, closed




def UnweightedAstarSearch(startidx, endidx, mapToSearch):

    try:
        selectedNode = Node(startidx, endidx, None, mapToSearch[startidx[0]][startidx[1]])

        open = MinHeap()

        openIndices = {}
        closed = {}

        while selectedNode.location != endidx:

            expansion = selectedNode.expandNode(openIndices, closed, mapToSearch, open)

            for node in expansion:
                open.insert(node)
                openIndices[node.location] = node

            selectedNode = open.remove()
            try:
                openIndices.pop(selectedNode.location)
            except:
                pass

            if len(openIndices) == 0:
                print("Sorry unreachable!")
                return openIndices, closed

            closed[selectedNode.location] = selectedNode


        print(backtrack(selectedNode, startidx, mapToSearch))

        return openIndices, closed
    except:
        print("Search Failed!")
        return None, closed




def WeightedAstarSearch(startidx, endidx, mapToSearch, weight):
    try:
        selectedNode = Node(startidx, endidx, None, mapToSearch[startidx[0]][startidx[1]], weight)

        open = MinHeap()

        openIndices = {}
        closed = {}


        while selectedNode.location != endidx:

            expansion = selectedNode.expandNode(openIndices, closed, mapToSearch, open)

            for node in expansion:
                open.insert(node)
                openIndices[node.location] = node

            selectedNode = open.remove()
            try:
                openIndices.pop(selectedNode.location)
            except:
                pass


            if len(openIndices) == 0:
                print("Sorry unreachable!")
                return openIndices, closed

            closed[selectedNode.location] = selectedNode


        print(backtrack(selectedNode, startidx, mapToSearch))

        return openIndices, closed
    except:
        print("search failed!")
        return None, closed


def Key(node, i, endidx, w1):
    g_val = node.distanceFromStartToCurrent[i]
    h_val = 0

    if i == 0:
        h_val = Node.calculateEuclideanHeuristic(node, endidx)
    elif i == 1:
        h_val = Node.calculateManhattanHeuristic(node, endidx)
    elif i == 2:
        h_val = Node.calculateOctileHeuristic(node, endidx)
    elif i == 3:
        h_val = Node.calculateChebyshevHeuristic(node, endidx)
    elif i == 4:
        h_val = Node.calculateBrayCurtisHeuristic(node, endidx)

    return g_val + w1 * h_val

def ExpandState(selectedNode, i, open, closed, endidx, mapToSearch, w1):
    for childNode in Node.expandNode(selectedNode, open, closed, mapToSearch):
        if childNode not in open and childNode not in closed:
            childNode.distanceFromStartToCurrent[i] = float('inf')
            childNode.bestparent[i] = None
        if childNode.distanceFromStartToCurrent[i] > selectedNode.distanceFromStartToCurrent[i] \
                + childNode.calculateDistanceFromParentToCurrent():
            childNode.distanceFromStartToCurrent[i] = selectedNode.distanceFromStartToCurrent[i] \
                                                      + childNode.calculateDistanceFromParentToCurrent()
            childNode.bestparent[i] = selectedNode
            if childNode not in closed:
                if childNode not in open:
                    heapq.heappush(open, (Key(selectedNode, i, endidx, w1), selectedNode))


def MultiHeuristicAStar(startidx, endidx, mapToSearch, w1, w2):
    startNode = Node(startidx, endidx, None, mapToSearch[startidx[0]][startidx[1]], False, True)
    goalNode = Node(endidx, endidx, None, mapToSearch[startidx[0]][startidx[1]], False, True)

    open = [[]] * 5
    closed = [[]] * 5

    for i in range(5):
        startNode.distanceFromStartToCurrent[i] = 0
        goalNode.distanceFromStartToCurrent[i] = float('inf')
        startNode.bestparent[i] = None
        goalNode.bestparent[i] = None
        heapq.heappush(open[i], (Key(startNode, i, endidx, w1), startNode))
        keys = [[]] * 5
    for node in open[0]:
        keys[0].append(Key(node, 0, endidx, w1))
    while min(keys[0]) < float('inf'):
        for i in range(1, 5):
            for node in open[i]:
                keys[i].append(Key(node, i, endidx, w1))
            if min(keys[i]) <= w2 * min(keys[0]):
                if goalNode.distanceFromStartToCurrent[i] <= min(keys[i]):
                    if goalNode.distanceFromStartToCurrent[i] <= float('inf'):
                        return goalNode.bestparent[i]
                else:
                    selectedNode = heapq.heappop(open[i])
                    ExpandState(selectedNode, i, open[i], closed[i])
                    closed[i].append(selectedNode)
            else:
                if goalNode.distanceFromStartToCurrent[0] <= min(keys[0]):
                    if goalNode.distanceFromStartToCurrent[0] <= float('inf'):
                        return goalNode.bestparent[0]
                else:
                    selectedNode = heapq.heappop(open[0])
                    ExpandState(selectedNode, 0, open[0], closed[0])
                    closed[0].append(selectedNode)
        keys[0].clear()
        for node in open[0]:
            keys[0].append(Key(node, 0, endidx, w1))







