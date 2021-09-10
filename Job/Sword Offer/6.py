# 从尾到头打印链表
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        ans.reverse()
        return ans


if __name__ == '__main__':
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    print(Solution().reversePrint(head))
