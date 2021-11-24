# 环形链表


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 快慢指针
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = fast = head
        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
            if slow == fast:
                return True
        return False

    # 另外一种写法
    def hasCycle2(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return False
        return True


if __name__ == '__main__':
    nodes = [3, 2, 0, -4]
    for i in range(len(nodes)):
        if i == 0:
            head = ListNode(nodes[i])
            dummy = head
        else:
            head.next = ListNode(nodes[i])
            head = head.next
    head.next = dummy
    print(Solution().hasCycle2(dummy))
