# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.arr=[]
        

    def push(self, x: int) -> None:
        self.arr.append(x)
        

    def pop(self) -> int:
        if self.arr:
            return self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def empty(self) -> bool:
        if len(self.arr) == 0:
            return True
        return False


        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()