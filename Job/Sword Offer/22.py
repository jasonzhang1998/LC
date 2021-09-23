# 链表的倒数第k个节点


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 快慢指针
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        pre = post = head
        for i in range(k):
            pre = pre.next
        while pre:
            pre = pre.next
            post = post.next
        return post


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().getKthFromEnd(head, 5).val)
