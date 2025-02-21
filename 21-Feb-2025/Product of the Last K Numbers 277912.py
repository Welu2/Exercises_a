# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.new=[1]
        

    def add(self, num: int) -> None:
        if num == 0:
            self.new=[1]
        else:
            self.new.append(num*self.new[-1])
       
        

    def getProduct(self, k: int) -> int:
    
        if k >= len(self.new):
            return 0
        return self.new[-1]//self.new[-(k+1)]

        