# 反转链表


# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 使用头插法新建一个链表
    def reverseList(self, head: ListNode) -> ListNode:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        for i in range(len(temp)):
            cur = ListNode(temp[i])
            cur.next = head
            head = cur
        return head

    # 使用三个指针直接对链表进行反转
    def reverseList2(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre = None
        cur = head
        pos = head.next
        # 只要cur不是最后一个节点，就继续修改指针
        while pos:
            # 将当前节点的next指向前一个节点，实现反转
            cur.next = pre
            pre = cur
            # print(pre.val)
            cur = pos
            pos = pos.next
        # 最后一个节点也需要反转
        cur.next = pre
        return cur


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = Solution().reverseList2(head)
    while res:
        print(res.val)
        res = res.next
