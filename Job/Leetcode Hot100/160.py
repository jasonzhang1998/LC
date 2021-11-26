# 相交链表


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 遍历链表，修改链表的值做标记
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ans = None
        dummy = headA
        while headA:
            headA.val = str(headA.val)
            headA = headA.next
        while headB:
            if type(headB.val) != type(1):
                ans = headB
                break
            else:
                headB = headB.next
        while dummy:
            dummy.val = int(dummy.val)
            dummy = dummy.next
        return ans if ans else None

    # 双指针法，两个指针分别两个头结点开始遍历，到底了之后换到另一个表头
    # 如果链表存在相交，那么中途就会在相交节点相遇，否则会都为空。
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1 if node1 else None


if __name__ == '__main__':
    head1 = ListNode(1)
    head1.next = ListNode(9)
    head1.next.next = ListNode(1)
    head1.next.next.next = ListNode(2)
    head2 = ListNode(3)
    head2.next = head1.next.next.next
    head1.next.next.next.next = ListNode(4)
    print(Solution().getIntersectionNode2(head1, head2).val)
