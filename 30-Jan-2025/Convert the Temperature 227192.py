# Problem: Convert the Temperature - https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:    
        k = celsius + 273.15
        f = celsius * 1.80 + 32.00
        return [k,f]
