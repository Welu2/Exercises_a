# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem=0
        dummy=ListNode(0)
        total=dummy
       
      
        while l1 or l2 or rem:
            s=rem
            if l1:
                s+=l1.val
                l1=l1.next
            if l2:
                s+=l2.val
                l2=l2.next

            rem = s//10
            newV=s%10
            total.next = ListNode(newV)
            total = total.next
      

        return dummy.next