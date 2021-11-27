# 反转链表


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 使用头插法反转链表
    # 利用一个虚拟的头结点，遍历链表，每次将遍历到的节点，先取出来，然后插到虚拟头结点之后
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        dummy = ListNode(next=head)
        cur = head.next
        while cur:
            head.next = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = head.next
        return dummy.next


if __name__ == '__main__':
    nodes = [1]
    for i in range(len(nodes)):
        if i == 0:
            head = ListNode(nodes[i])
            dummy = head
        else:
            head.next = ListNode(nodes[i])
            head = head.next
    x = Solution().reverseList(dummy)
    while x:
        print(x.val, end=' -> ')
        x = x.next
