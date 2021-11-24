# 环形链表


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 暴力解法，使用一个set来存储访问过的节点
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        while head:
            if head in visited:
                return head
            else:
                visited.add(head)
                head = head.next
        return head

    # 常量空间复杂度的解法，快慢指针
    def detectCycle2(self, head: ListNode) -> ListNode:
        if not head:
            return
        fast = slow = head
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return

            if slow == fast:
                temp = head
                while temp != slow:
                    temp = temp.next
                    slow = slow.next
                return slow
        return


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
    print(Solution().detectCycle2(dummy))
