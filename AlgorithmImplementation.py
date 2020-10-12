import math
import constants
from MinHeap import MinHeap
from Node import *


def backtrack(node: Node, startidx: tuple, mapToSearch):

    #Recursively call backtrack until we reach a node with start idx
    if node.location == startidx:
        mapToSearch[node.location[0]][node.location[1]] = 'optimal'
        return node.location
    mapToSearch[node.location[0]][node.location[1]] = 'optimal'
    return f"{node.location} {backtrack(node.parent, startidx, mapToSearch)}"




def UniformCost(startidx, endidx):
    pass




# TODO: Need to modify this code for weighted search
def UnweightedAstarSearch(startidx, endidx, mapToSearch):

    # Selected Node will be initialized to the start node
    selectedNode = Node(startidx, endidx, None)

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


# Exactly the same as unweighted Astar but we set the value of weight > 1
def WeightedAstarSearch(startidx, endidx, mapToSearch, weight):
    # Selected Node will be initialized to the start node
    selectedNode = Node(startidx, endidx, None)
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


if __name__ == "__main__":
    UnweightedAstarSearch((0,0), (119,159))






