# 对链表进行插入排序

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        ret = ListNode()
        while dummy.next:
            # 取出待排序元素，并将其从原链表删除
            node = dummy.next
            dummy.next = node.next

            # cur用于寻找待排序节点的插入位置
            cur = ret.next
            # pre用于辅助插入节点
            pre = ret
            while cur and node.val > cur.val:
                pre, cur = pre.next, cur.next
            node.next = pre.next
            pre.next = node
        return ret.next
