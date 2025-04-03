# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        curent=head
        while curent:
            arr.append(curent.val)
            curent=curent.next
        arr.sort()
        l=0
        current=head
        while current:
            current.val=arr[l]
            l+=1
            current=current.next
        


        return head
