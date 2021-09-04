# 环形链表


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 快慢指针，注意条件判断
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # if not head:
        #     return False
        # slow = head.next
        # if slow and slow.next:
        #     fast = slow.next
        # else:
        #     return False
        if not head or not head.next:
            return False
        fast = head.next
        slow = head
        while fast != slow:
            if fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return False
        return True


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    x = Solution().hasCycle(root)
    print(x)
