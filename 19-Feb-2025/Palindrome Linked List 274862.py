# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length=0
        current = head
        while current:
            length+=1
            current=current.next
        h=length//2
        arr=[]
        current=head
        for _ in range(h):
            arr.append(current.val)
            current=current.next
       
        if length % 2 == 0:
            l=-1
            while current:
                if arr[l] != current.val:
                    return False
                l-=1    
                current=current.next
            
            return True
        else:
            current=current.next
            l=-1
            while current:   
                if arr[l] != current.val:
                    return False
                l-=1
                current=current.next
                
            
            return True
