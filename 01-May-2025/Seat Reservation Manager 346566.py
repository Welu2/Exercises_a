# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        nums=[i for i in range(1,n+1)]
        self.min_heap = nums
        heapq.heapify(self.min_heap)


        

    def reserve(self) -> int:
        val=heapq.heappop(self.min_heap)
        return val
        

    def unreserve(self, seatNumber: int) -> None:
     
        heapq.heappush(self.min_heap,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)