# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        def reverse(curr):
            if not curr.next:
                return curr

            new_head = reverse(curr.next)
            curr.next.next = curr
            curr.next = None

            return new_head 
        return reverse(head)

        
