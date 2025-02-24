# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddOne=ListNode()
        evenone =ListNode()
        odd=oddOne
        even = evenone
        current=head
        idx=0
        while current:
            if idx % 2 ==0:
                even.next=current
                even=even.next
            else:
                odd.next=current
                odd=odd.next
            idx+=1
            current=current.next

        odd.next=None
        
        even.next=oddOne.next
        
        
        return evenone.next
        