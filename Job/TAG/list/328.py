# 奇偶链表


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 将链表先按奇偶元素分开，然后再连一块
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy1 = ListNode()
        dummy2 = ListNode()
        count = 1
        cur = head
        tail1, tail2 = dummy1, dummy2
        while cur:
            temp = cur.next
            cur.next = None
            if count % 2 == 1:
                tail1.next = cur
                tail1 = tail1.next
            else:
                tail2.next = cur
                tail2 = tail2.next
            cur = temp
            count += 1
        tail1.next = dummy2.next
        return dummy1.next
