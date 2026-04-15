# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if not head.next:
        #     return head
        slow = fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        slow.next = None
        l1 = head
        # if not l2:
        #     return l1
        # if not l2.next:
        #     curr = l1
        #     nxt = curr.next
        #     curr.next = l2
        #     curr.next.next = nxt
        #     return l1

        prev = None
        curr = l2
        if l2:
            nxt = l2.next

        while curr:
            curr.next = prev
            prev = curr
            curr = nxt
            if nxt:
                nxt = nxt.next
        

        p1 = l1
        p2 = prev
        

        while p1 and p2:
            nxt = p1.next #2
            nxt2 = p2.next
            p1.next = p2 #1 => 5
            p1.next.next = nxt # 1 => 5 => 2
            p1 = p1.next.next # 2
            p2 = nxt2 # 4
            

        # return l1

