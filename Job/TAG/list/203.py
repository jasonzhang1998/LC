# 移除链表元素

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(next=head)
        pre = dummy
        while pre.next:
            cur = pre.next
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
        return dummy.next
