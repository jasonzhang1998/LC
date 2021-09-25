# 合并两个排序的链表


# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLlists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        dummy = head
        while l1 or l2:
            if not l2:
                cur = ListNode(l1.val)
                l1 = l1.next
            elif not l1:
                cur = ListNode(l2.val)
                l2 = l2.next
            elif l1.val < l2.val:
                cur = ListNode(l1.val)
                l1 = l1.next
            else:
                cur = ListNode(l2.val)
                l2 = l2.next
            head.next = cur
            head = head.next
        return dummy.next

    # 优化1：某链表合并结束后，剩下的链表直接接到合并链表的尾部，无需放在循环内
    # 优化2：合并链表的时候无需新建节点
    def mergeTwoLlists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        cur = head
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return head.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    x = Solution().mergeTwoLlists2(l1, l2)
    while x:
        print(x.val)
        x = x.next
