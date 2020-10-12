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

    # Open can be a Min. Heap
    open = MinHeap()
    closed = []

    # TODO: ALSO NEVER CHECKED IF CELL IS BLOCKED
    while selectedNode.location != endidx:

        for node in selectedNode.expandNode(open.minheap, closed):
           open.insert(node)

        selectedNode = open.minheap[0]
        open.remove()
        closed.append(selectedNode)

    print(backtrack(selectedNode, startidx))





if __name__ == "__main__":
    UnweightedAstarSearch((0,0), (50,55))







"""

Code from Unweighted A*Star:
 for node in open:
            if node.sumOfHeuristicAndDistanceFromStartToCurrent <= selectedNode.sumOfHeuristicAndDistanceFromStartToCurrent:
                idxToExpand = idx
            idx += 1




"""