# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calulate_days(mid_weight):
            day=1
            total=0
            for i in weights:
                total+=i
                if total > mid_weight:
                    day+=1
                    total=i
                   
            return day    

        min_weight=max(weights)
        max_weight=sum(weights)
        perfect_weight=float("inf")
        while min_weight <= max_weight:
            mid_weight=(min_weight+max_weight)//2
            if calulate_days(mid_weight) > days:
                min_weight=mid_weight+1
            else:
                perfect_weight=min(perfect_weight,mid_weight)
                max_weight=mid_weight-1
               
        return perfect_weight
