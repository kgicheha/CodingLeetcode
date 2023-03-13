class minHeap:
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    #HELPER METHODS
    def getParentIndex(self, index):
        return (index - 1) // 2

    def leftChildIndex(self, index):
        return 2 * index + 1

    def rightChildIndex(self, index):
        return 2 * index + 2

    def hasParent(self,index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    # def parent(self, index)