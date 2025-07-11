# Problem: Smallest Number in Infinite Set - https://leetcode.com/problems/smallest-number-in-infinite-set/description/

class SmallestInfiniteSet:

    def __init__(self):
        self.current=1
        self.added_back_set = set()
        self.min_heap = []

    def popSmallest(self) -> int:
        if self.min_heap:
            smallest = heapq.heappop(self.min_heap)
            self.added_back_set.remove(smallest)
            return smallest
        else:
            val = self.current
            self.current += 1
            return val
        

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added_back_set:
            heapq.heappush(self.min_heap, num)
            self.added_back_set.add(num)

            
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)