# 两个链表的第一个公共节点

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 先遍历其中一条链表，将所有节点的val由int改为str
    # 再遍历另外一条链表，遇到的第一个节点值类型为str的节点就是第一个相交节点
    # 须保持原链表不变，所以还得把第一遍遍历的链表改回来
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dummy = headA
        while dummy:
            tmp = dummy.val
            dummy.val = str(tmp)
            dummy = dummy.next
        head = headB
        ans = None
        while head:
            if type(head.val) is str:
                ans = head
                break
            head = head.next
        dummy = headA
        while dummy:
            tmp = dummy.val
            dummy.val = int(dummy.val)
            dummy = dummy.next
        return ans

    # 双指针法，两个指针分别指向两个链表的头结点，依次往后移动
    # 如果某个指针为空，则将其移到另一个链表的头结点
    # 假设链表长度分别为m, n，那么最多走m + n步，两个指针就会相遇
    # 如果两个链表相交，那么指针会在某个中间时刻相遇，这时共同指向的节点就是
    # 第一个公共节点。如果不相交，那么最终两个指针都会指向空
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1


if __name__ == '__main__':
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = ListNode(8)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)
    headB = ListNode(5)
    headB.next = ListNode(0)
    headB.next.next = ListNode(1)
    headB.next.next.next = headA.next.next
    x = Solution().getIntersectionNode2(headA, headB)
    print(x.val)
    # while headB:
    #     print(headB.val)
    #     headB = headB.next
