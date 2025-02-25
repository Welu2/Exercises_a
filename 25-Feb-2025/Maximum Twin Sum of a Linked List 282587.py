# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse(head):
            current=head
            prev=None
            while current:
                nextV=current.next
                current.next=prev
                prev=current
                current=nextV
            return prev
        
        slow=head
        fast=head
        second=ListNode()
        elem=second
        while fast:
            slow=slow.next
            fast=fast.next.next

        t=slow
        while t:
            elem.next=t
            elem=elem.next
            t=t.next
 
        elem.next=None
        reversed=reverse(second.next)
        current=head
        maxV=0
        while reversed:
            maxV=max(maxV,(reversed.val+current.val))
            reversed=reversed.next
            current=current.next

        return maxV
