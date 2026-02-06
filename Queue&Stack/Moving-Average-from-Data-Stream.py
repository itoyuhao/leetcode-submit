# https://leetcode.com/problems/moving-average-from-data-stream/description/
class MovingAverage:

    def __init__(self, size: int):
        self.queue = [0] * size
        self.head = 0
        self.count = 0
        self.capacity = size
        
        
    def next(self, val: int) -> float:        
        self.queue[(self.head + self.count) % self.capacity] = val
        self.count += 1
        return sum(self.queue) / min(self.count, self.capacity)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)