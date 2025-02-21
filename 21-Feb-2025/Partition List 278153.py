# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]: 
        lessElements=ListNode()
        greatElements=ListNode()
        
        less=lessElements
        great=greatElements

        current=head
        while current:
            if current.val < x:
                less.next=current
                less=less.next
            else:
                great.next=current
                great=great.next
            current=current.next
        
        great.next=None
        less.next=greatElements.next
        return lessElements.next
       