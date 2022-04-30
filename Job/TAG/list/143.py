# 重排链表

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 重排链表本质上就是把链表尾部的节点插到链表头部
    # 用栈保存需要插入的节点，然后逐个插入
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        stack = []
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        # print(slow.val)
        slow.next = None
        while temp:
            node = temp.next
            temp.next = None
            stack.append(temp)
            temp = node
        cur = head
        # print(stack)
        while stack:
            node = stack.pop()
            node.next = cur.next
            cur.next = node
            cur = cur.next.next
        return head

    # 可以不用栈保存后半部分链表，而是将其反转
    def reorderList2(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(head):
            if not head or not head.next:
                return head
            dummy = ListNode(next=head)
            pre = head
            while pre.next:
                cur = pre.next
                pre.next = cur.next
                cur.next = dummy.next
                dummy.next = cur
            return dummy.next

        if not head or not head.next:
            return head
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        new_head = reverse(temp)
        cur = head
        while new_head:
            temp = new_head.next
            new_head.next = cur.next
            cur.next = new_head
            new_head = temp
            cur = cur.next.next
        return head


