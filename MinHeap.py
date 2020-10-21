from Node import Node




class MinHeap():

    def __init__(self):
        self.minheap = []


    def sift_up(self, idx):

        while idx // 2 > 0:
            if self.minheap[idx].sumOfHeuristicAndDistanceFromStartToCurrent < self.minheap[idx // 2].sumOfHeuristicAndDistanceFromStartToCurrent:
                self.minheap[idx // 2], self.minheap[idx] = self.minheap[idx], self.minheap[idx // 2]

            idx = idx // 2


    def sift_down(self, idx):
        child1 = idx * 2 + 1
        child2 = idx * 2 + 2

        try:
            greaterChild = child1 if self.minheap[child1].sumOfHeuristicAndDistanceFromStartToCurrent <= self.minheap[child2].sumOfHeuristicAndDistanceFromStartToCurrent else child2
            self.swap(idx, greaterChild)
            self.sift_down(greaterChild)

        # Index out of bounds error
        except IndexError:
            return


    def swap(self, a, b):
        temp = self.minheap[a]
        self.minheap[a] = self.minheap[b]
        self.minheap[b] = temp

    def insert(self, state: Node):


        self.minheap.append(state)
        if len(self.minheap) > 1:
            self.sift_up(len(self.minheap) - 1)

    def remove(self):

        if len(self.minheap) > 0:
            self.swap(0, len(self.minheap) - 1)
            node = self.minheap.pop()
            self.sift_down(0)
            return node
        else:
            print("Heap is Empty!")


class MinHeapForUniform(MinHeap):


    def sift_up(self, idx):

        while idx // 2 > 0:
            if self.minheap[idx].distanceFromStartToCurrent < self.minheap[idx // 2].distanceFromStartToCurrent :
                self.minheap[idx // 2], self.minheap[idx] = self.minheap[idx], self.minheap[idx // 2]

            idx = idx // 2

        return

    def sift_down(self, idx):
        child1 = idx * 2 + 1
        child2 = idx * 2 + 2

        try:
            greaterChild = child1 if self.minheap[child1].distanceFromStartToCurrent <= self.minheap[child2].distanceFromStartToCurrent else child2
            self.swap(idx, greaterChild)
            self.sift_down(greaterChild)

        # Index out of bounds error
        except IndexError:
            return
