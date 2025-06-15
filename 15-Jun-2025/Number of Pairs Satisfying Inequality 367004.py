# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        arr = [nums1[i] - nums2[i] for i in range(n)]
    
        def merge_sort(enum):
            if len(enum) <= 1:
                return enum, 0
            mid = len(enum) // 2
            left, count_left = merge_sort(enum[:mid])
            right, count_right = merge_sort(enum[mid:])
            count = count_left + count_right
            
            j = 0
            for i in range(len(left)):
                while j < len(right) and right[j][1] < left[i][1] - diff:
                    j += 1
                count += len(right) - j
            
            # Merge step
            merged = []
            l = r = 0
            while l < len(left) and r < len(right):
                if left[l][1] <= right[r][1]:
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
            merged += left[l:]
            merged += right[r:]
            
            return merged, count

        # Pair each value with its index
        _, total_count = merge_sort(list(enumerate(arr)))
        return total_count