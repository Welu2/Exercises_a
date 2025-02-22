# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
class MyLinkedList:

    def __init__(self):
       self.dummy = Node()
       self.tail = None
       self.count= 0
    def get(self, index: int) -> int:
        if index >=self.count :
            return -1
        curr_idx = 0
        curr_node =self.dummy.next
        while curr_idx < index :
            curr_node = curr_node.next
            curr_idx +=1
        return curr_node.val
    def addAtHead(self, val: int) -> None:
        head = self.dummy.next
        newnode = Node(val)
        self.dummy.next = newnode
        newnode.next= head
        self.count += 1
        if not self.tail:
            self.tail= newnode

    def addAtTail(self, val: int) -> None:
        newnode = Node(val)
        if not self.tail:
            self.dummy.next = newnode
            self.tail = newnode
        else :
            self.tail.next = newnode
            self.tail=newnode
        self.count += 1
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return 
        if index == self.count :
            self.addAtTail(val)
        else:
            curr_idx = 0
            curr_node =self.dummy
            while curr_idx < index :
                curr_node = curr_node.next
                curr_idx +=1
            newnode = Node(val)
            newnode.next=  curr_node.next
            curr_node.next = newnode
            self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.count:
            return 
        curr_idx = 0
        curr_node =self.dummy
        while curr_idx < index :
            curr_node = curr_node.next
            curr_idx +=1
        curr_node.next = curr_node.next.next
        if not curr_node.next:
            self.tail = curr_node
        self.count -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)