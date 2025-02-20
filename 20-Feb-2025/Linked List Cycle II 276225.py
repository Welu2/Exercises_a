# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        def cycle(slow,fast):
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
                if slow == fast:
                    return fast
            return False
        if not cycle(slow,fast):
            return 
        else:
            fast=cycle(slow,fast)
            slow=head
            while slow != fast:
                slow = slow.next
                fast=fast.next


        return slow