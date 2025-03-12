# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.backward=[homepage]
        self.forw=[]

    def visit(self, url: str) -> None:
        self.backward.append(url)
        self.forw=[]
        

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.backward) > 1 :
            self.forw.append(self.backward.pop())
            steps-=1

        return self.backward[-1] 
        

    def forward(self, steps: int) -> str:
        while steps > 0 and len(self.forw) > 0:
            self.backward.append(self.forw.pop())
            steps -= 1
        return self.backward[-1] if self.backward else ''
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)