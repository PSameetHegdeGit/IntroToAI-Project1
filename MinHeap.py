from Node import Node


class MinHeap():

    minheap: list[Node] = []

    def insert(self, state: Node):

        def heapify(self, lastidx):
            prtIdx = (lastidx - 1) / 2 if lastidx % 2 != 0 else (lastidx - 2) / 2

            if self.minheap[prtIdx].sumOfHeuristicAndDistanceFromStartToCurrent < self.minheap[
                lastidx].sumOfHeuristicAndDistanceFromStartToCurrent:
                self.swap(prtIdx, lastidx)
                self.heapify(prtIdx)

            return



        self.minheap.append(state)
        heapify(len(self.minheap) - 1)

    def remove(self):

        def readjustMinHeapAfterDeletion(self, idx):
            child1 = idx * 2 + 1
            child2 = idx * 2 + 2

            try:
                greaterChild = child1 if self.minheap[child1].sumOfHeuristicAndDistanceFromStartToCurrent <= self.minheap[child2].sumOfHeuristicAndDistanceFromStartToCurrent else child2
                self.swap(idx, greaterChild)
                self.readjustMinHeapAfterDeletion()

            # Index out of bounds error
            except IndexError:
                return

        if len(self.minheap) > 0:
            self.swap(0, len(self.minheap) - 1)
            readjustMinHeapAfterDeletion(0)
        else:
            print("Heap is Empty!")



    def swap(self, a, b):
        temp = self.minheap[a]
        self.minheap[a] = self.minheap[b]
        self.minheap[b] = temp



