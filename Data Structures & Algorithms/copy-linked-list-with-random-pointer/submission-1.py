# """
# # Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
# """

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return

        curr = head
        # do the next pointer
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
            
        # do the random pointer
        curr = head 

        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        
        # split the copy and original

        # 3 =>  3 =>  7 => 7
        # 3 => 7
        curr = head
        newHead = head.next
        newCurr = newHead

        while curr:
            curr.next = newCurr.next
            curr = curr.next
            if curr:
                newCurr.next = curr.next
                newCurr = newCurr.next

        return newHead

   