class MedianFinder:

    def __init__(self):
        self.list = []
        

    def addNum(self, num: int) -> None:
        self.list.append(num)
        

    def findMedian(self) -> float:
        self.list.sort()
        size = len(self.list)
        if size % 2 == 0:
            b = int(size / 2)
            return (self.list[b - 1] + self.list[b]) / 2
        else:
            return self.list[int(size / 2)]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()