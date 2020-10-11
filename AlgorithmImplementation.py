import math
import constants
from MinHeap import MinHeap
from Node import Node


def backtrack(node: Node, startidx: tuple):

    #Recursively call backtrack until we reach a node with start idx
    if node.location == startidx:
        return node.location
    return f"{node.location} {backtrack(node.parent, startidx)}"





# TODO: Need to modify this code for weighted search
def UnweightedAstarSearch(startidx, endidx):

    # Selected Node will be initialized to the start node
    selectedNode = Node(startidx, endidx, None)

    open = []
    closed = []

    # TODO: ALSO NEVER CHECKED IF CELL IS BLOCKED
    while selectedNode.location != endidx:

        open.extend(selectedNode.expandNode(open, closed))
        closed.append(selectedNode)

        idxToExpand = 0
        idx = 0

        for node in open:
            if node.sumOfHeuristicAndDistanceFromStartToCurrent <= selectedNode.sumOfHeuristicAndDistanceFromStartToCurrent:
                idxToExpand = idx
            idx += 1

        selectedNode = open[idxToExpand]
        closed.append(selectedNode)
        open.remove(open[idxToExpand])


    print(backtrack(selectedNode, startidx))





if __name__ == "__main__":
    # UnweightedAstarSearch((0,0), (10,23))

    pass
