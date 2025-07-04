# Problem: The Number of the Smallest Unoccupied Chair - https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n= len(times)
        events = []
    
    # Step 1: Collect all events
        for friend, (arrive, leave) in enumerate(times):
            events.append((arrive, 'arrive', friend))
            events.append((leave, 'leave', friend))
        
        # Step 2: Sort events
        events.sort()

        # Step 3: Initialize structures
        available_chairs = list(range(n))  # At most n chairs needed
        heapq.heapify(available_chairs)
        
        friend_to_chair = {}
        occupied = []

        for time, event_type, friend in events:
            # Free chairs from friends who have left
            while occupied and occupied[0][0] <= time:
                leave_time, chair = heapq.heappop(occupied)
                heapq.heappush(available_chairs, chair)

            if event_type == 'arrive':
                chair = heapq.heappop(available_chairs)
                friend_to_chair[friend] = chair
                heapq.heappush(occupied, (times[friend][1], chair))
                if friend == targetFriend:
                    return chair

        return -1  # Should never reach here