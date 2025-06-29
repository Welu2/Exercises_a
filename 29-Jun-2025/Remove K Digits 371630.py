# Problem: Remove K Digits - https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # Remove remaining digits if needed
        stack = stack[:-k] if k else stack

        # Remove leading zeros
        result = ''.join(stack).lstrip('0')

        return result if result else '0'
            