# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans=[]
        for l in lists:

            current=l
            while current:
                ans.append(current.val)
                current=current.next

        heapq.heapify(ans)
        answer=ListNode()
        current=answer
        while ans:
            if heapq:
                current.next=ListNode(heapq.heappop(ans))
                current =current.next
        return answer.next