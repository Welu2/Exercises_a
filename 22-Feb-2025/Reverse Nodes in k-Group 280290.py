# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node):
            current=head
            prev=None
            while current:
                nextnode=current.next
                current.next=prev
                prev=current
                current=nextnode

            return prev

        length=0
        dummy=ListNode()
        dummy.next=head
        kones=dummy
        
        current=head
        
        
        while head:
            current = head
            count=0
            while count < k and current:
                current = current.next
                count += 1

   
            if count == k:
                kgroup=head
                for _ in range(k - 1): 
                    kgroup = kgroup.next
                next_group = kgroup.next
                kgroup.next = None
                new_group_head = reverse(head)
                 # Connect the reversed group back to the list
                kones.next = new_group_head
                head.next = next_group
              
                # Move prev_group and head for the next round of reversal
                kones = head
                head = next_group
            else:
                # Not enough nodes to fill a k group, so we are done
                break
                
        return dummy.next
        
        


        