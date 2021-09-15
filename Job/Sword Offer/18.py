# 删除链表的节点


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        if head.val == val:
            return head.next
        pre = head
        pos = head.next
        while pos:
            if pos.val == val:
                pre.next = pos.next
            pre = pos
            pos = pos.next
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = Solution().deleteNode(head, 5)
    while res:
        print(res.val)
        res = res.next
