import math
import constants
from MinHeap import *
from Node import *


def backtrack(node: Node, startidx: tuple, mapToSearch):

    #Recursively call backtrack until we reach a node with start idx
    if node.location == startidx:
        mapToSearch[node.location[0]][node.location[1]] = 'optimal'
        return node.location
    mapToSearch[node.location[0]][node.location[1]] = 'optimal'
    return f"{node.location} {backtrack(node.parent, startidx, mapToSearch)}"




def UniformCost(startidx, endidx, mapToSearch):
    # Selected Node will be initialized to the start node
    selectedNode = UniformCostNode(startidx, endidx, None, mapToSearch[startidx[0]][startidx[1]])

    # Open is a Min. Heap
    open = MinHeapForUniform()

    # Using dictionary instead of array to improve search time; having a separate heap and openindices
    openIndices = {}
    closed = {}

    # TODO: ALSO NEVER CHECKED IF CELL IS BLOCKED
    while selectedNode.location != endidx:

        expansion = selectedNode.expandNode(openIndices, closed, mapToSearch)

        for node in expansion:
            open.insert(node)
            openIndices[node.location] = node

        selectedNode = open.minheap[0]
        open.remove()
        closed[selectedNode.location] = selectedNode

    print(backtrack(selectedNode, startidx, mapToSearch))
    return openIndices, closed




# TODO: Need to modify this code for weighted search
def UnweightedAstarSearch(startidx, endidx, mapToSearch):

    # Selected Node will be initialized to the start node
    selectedNode = Node(startidx, endidx, None, mapToSearch[startidx[0]][startidx[1]])

    # Open is a Min. Heap
    open = MinHeap()

    # Using dictionary instead of array to improve search time; having a separate heap and openindices
    openIndices = {}
    closed = {}

    # TODO: ALSO NEVER CHECKED IF CELL IS BLOCKED
    while selectedNode.location != endidx:

        expansion = selectedNode.expandNode(openIndices, closed, mapToSearch)

        for node in expansion:
            open.insert(node)
            openIndices[node.location] = node

        selectedNode = open.minheap[0]
        open.remove()
        closed[selectedNode.location] = selectedNode

    print(backtrack(selectedNode, startidx, mapToSearch))
    return openIndices, closed



# Exactly the same as unweighted Astar but we set the value of weight > 1
def WeightedAstarSearch(startidx, endidx, mapToSearch, weight):
    # Selected Node will be initialized to the start node
    selectedNode = Node(startidx, endidx, None, mapToSearch[startidx[0]][startidx[1]])
    selectedNode.weight = weight

    # Open is a Min. Heap
    open = MinHeap()

    # Using dictionary instead of array to improve search time; having a separate heap and openindices
    openIndices = {}
    closed = {}

    # TODO: ALSO NEVER CHECKED IF CELL IS BLOCKED
    while selectedNode.location != endidx:

        expansion = selectedNode.expandNode(openIndices, closed, mapToSearch)

        for node in expansion:
            open.insert(node)
            openIndices[node.location] = node

        selectedNode = open.minheap[0]
        open.remove()
        closed[selectedNode.location] = selectedNode

    print(backtrack(selectedNode, startidx, mapToSearch))
    return openIndices, closed

def Key(idx, i, open, closed, w1):
    g_val = 0
    h_val = 0
    if idx in open:
        g_val = open[idx].distanceFromStartToCurrent
    elif idx in closed:
        g_val = open[idx].distanceFromStartToCurrent

    if i == 0:
        h_val = Node.calculateEuclideanHeuristic(Node, idx)
    elif i == 1:
        h_val = Node.calculateManhattanHeuristic(Node, idx)
    elif i == 2:
        h_val = Node.calculateCanberraHeuristic(Node, idx)
    elif i == 3:
        h_val = Node.calculateChebyshevHeuristic(Node, idx)
    elif i == 4:
        h_val = Node.calculateBrayCurtisHeuristic(Node, idx)

    return g_val + w1 * h_val

def MultiHeuristicAStar(startidx, endidx, mapToSearch, w1, w2):
    selectedNode = Node(startidx, endidx, None, mapToSearch[startidx[0]][startidx[1]], False, True)

    open = [MinHeap()] * 5

    openIndices = [{}] * 5
    closed = [{}] * 5

    for i in range(5):
        print("open", open[i].minheap)
        print("open indices", openIndices[i])
        print("closed", closed[i])


if __name__ == "__main__":
    UnweightedAstarSearch((0,0), (119,159))






