# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

   n = len(nums)
    count = 0

    for i in range(n):
        current_gcd = 0
        for j in range(i, n):
            current_gcd = gcd(current_gcd, nums[j])
            if current_gcd < k:
                break
            if current_gcd == k:
                count += 1

    return count