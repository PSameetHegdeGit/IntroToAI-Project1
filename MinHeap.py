from Node import Node


class MinHeap():

    minheap = []

    def heapify(self, idx):
        prtIdx = int((idx - 1) / 2) if idx % 2 != 0 else int((idx - 2) / 2)

        if self.minheap[prtIdx].sumOfHeuristicAndDistanceFromStartToCurrent < self.minheap[idx].sumOfHeuristicAndDistanceFromStartToCurrent:
            self.swap(prtIdx, idx)
            self.heapify(prtIdx)

        return

    def readjustMinHeapAfterDeletion(self, idx):
        child1 = idx * 2 + 1
        child2 = idx * 2 + 2

        try:
            greaterChild = child1 if self.minheap[child1].sumOfHeuristicAndDistanceFromStartToCurrent <= self.minheap[
                child2].sumOfHeuristicAndDistanceFromStartToCurrent else child2
            self.swap(idx, greaterChild)
            self.readjustMinHeapAfterDeletion(greaterChild)

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
            self.heapify(len(self.minheap) - 1)

    def remove(self):

        if len(self.minheap) > 0:
            self.swap(0, len(self.minheap) - 1)
            self.minheap.pop()
            self.readjustMinHeapAfterDeletion(0)
        else:
            print("Heap is Empty!")


class MinHeapForUniform(MinHeap):


    def heapify(self, idx):
        prtIdx = int((idx - 1) / 2) if idx % 2 != 0 else int((idx - 2) / 2)

        if self.minheap[prtIdx].distanceFromStartToCurrent < self.minheap[idx].distanceFromStartToCurrent:
            self.swap(prtIdx, idx)
            self.heapify(prtIdx)

        return

    def readjustMinHeapAfterDeletion(self, idx):
        child1 = idx * 2 + 1
        child2 = idx * 2 + 2

        try:
            greaterChild = child1 if self.minheap[child1].distanceFromStartToCurrent <= self.minheap[child2].distanceFromStartToCurrent else child2
            self.swap(idx, greaterChild)
            self.readjustMinHeapAfterDeletion(greaterChild)

        # Index out of bounds error
        except IndexError:
            return





