# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low=0
        high=max(ranks)*(cars**2)
        min_t=high
        def check(mid):
            total_cars=0
            for i in ranks:
                total_cars+=(int(sqrt(mid/i)))
            return total_cars >= cars
            

        while low <= high :
            mid =(low+high)//2
            if check(mid):
                min_t=mid
                high=mid-1
            else:
                low=mid+1

        return min_t


