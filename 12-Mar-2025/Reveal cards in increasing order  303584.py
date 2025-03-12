# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        arr=[0]*(len(deck))
        deck.sort()
        queue = deque()  
        for i in range(len(deck)):
            queue.append(i)
      
        for card in deck:
           
            position = queue.popleft()
 
            arr[position] = card
        
            if queue:
                queue.append(queue.popleft())
        
        return arr