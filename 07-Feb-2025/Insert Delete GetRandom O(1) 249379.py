# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.hashset={}
        self.lst=list()
        

    def insert(self, val: int) -> bool:
        if val not in self.hashset:
            self.lst.append(val)
            self.hashset[val]=len(self.lst)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.lst:
            index=self.hashset[val]
            self.lst[index],self.lst[-1] =self.lst[-1],self.lst[index]
            
            self.hashset[self.lst[index]] = index
            self.lst.pop()

            del self.hashset[val]
            return True
        return False
        

    def getRandom(self) -> int:
        if not self.hashset:
            raise ValueError("HashSet is empty")
        random_index = random.choice(list(self.hashset.values()))
        return self.lst[random_index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()