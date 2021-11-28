# 回文链表


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 先将链表的后半部分翻转，然后判断是不是回文链表
    # 最后将后半部分翻转回来，返回结果
    def isPalindrome(self, head: ListNode) -> bool:
        def reverseList(node):
            if not node:
                return node
            dummy = ListNode(next=node)
            cur = node.next
            while cur:
                node.next = cur.next
                cur.next = dummy.next
                dummy.next = cur
                cur = node.next
            return dummy.next

        if not head or not head.next:
            return True
        dummy = ListNode(next=head)
        slow = dummy
        fast = head
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
        slow.next = reverseList(slow.next)
        pre = head
        pos = slow.next
        while pre and pos:
            if pre.val != pos.val:
                return False
            pre = pre.next
            pos = pos.next
        slow.next = reverseList(slow.next)
        return True


if __name__ == '__main__':
    nodes = [1, 2, 2, 1]
    for i in range(len(nodes)):
        if i == 0:
            head = ListNode(nodes[i])
            dummy = head
        else:
            head.next = ListNode(nodes[i])
            head = head.next
    print(Solution().isPalindrome(dummy))
    x = 1
