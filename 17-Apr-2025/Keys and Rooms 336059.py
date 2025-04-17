# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue=deque([0])
        n=len(rooms)
        unlocked=set()
        unlocked.add(0)

        while queue:
            key= queue.popleft()
            for k in rooms[key]:
                if k not in unlocked:
                    unlocked.add(k)
                    queue.append(k)
                   


    
        return len(unlocked) == n