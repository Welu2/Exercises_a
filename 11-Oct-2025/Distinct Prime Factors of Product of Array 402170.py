# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        arr=[True for _ in range(max(nums)+1)]
        arr[0] = arr[1] = False
        for i in range(2, int(len(arr) ** 0.5) + 1):
            if arr[i]:
                for j in range(i * i, len(arr), i):
                    arr[j] = False
        prime_factors = set()

        for num in nums:
            n = num
            for p in range(2, int(n ** 0.5) + 1):
                if arr[p] and n % p == 0:
                    prime_factors.add(p)
                    while n % p == 0:
                        n //= p
            if n > 1:
                prime_factors.add(n)

        return len(prime_factors)
