# 反转链表


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 头插法建立一个新链表
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = None
        while head:
            node = ListNode(head.val, dummy)
            dummy = node
            head = head.next
        return dummy

    # 使用三个指针迭代地反转链表
    def reverseList2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = None
        cur = head
        pos = head.next
        while cur:
            cur.next = pre
            pre = cur
            cur = pos
            if pos:
                pos = pos.next
        return pre

    # 递归地反转链表
    # 首先将大问题转换成子问题，将问题不断变小，这是 “递” 的过程
    # 然后找到最小的子问题，即递归终止条件
    # 然后定义解决子问题的操作，不断扩大子问题规模。这是 “归” 的过程
    def reverseList3(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = self.reverseList3(head.next)
        head.next.next = head
        head.next = None
        return dummy


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    x = Solution().reverseList3(head)
    while x:
        print(x.val)
        x = x.next
