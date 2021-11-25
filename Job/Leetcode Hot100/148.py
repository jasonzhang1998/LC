# 排序链表


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 自顶向下归并排序
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sortHelper(node):
            if not node or not node.next:
                return node
            fast = slow = node
            fast = fast.next.next
            while fast:
                if fast.next:
                    fast = fast.next.next
                else:
                    break
                slow = slow.next
            node1 = slow.next
            slow.next = None
            left = sortHelper(node)
            right = sortHelper(node1)

            dummy = ListNode()
            head = dummy
            while left and right:
                if left.val < right.val:
                    dummy.next = left
                    left = left.next
                else:
                    dummy.next = right
                    right = right.next
                dummy = dummy.next
            if not left and not right:
                return head.next
            elif left:
                dummy.next = left
            elif right:
                dummy.next = right
            return head.next

        return sortHelper(head)

    # 自底向上
    def sortList2(self, head: ListNode) -> ListNode:
        # 合并两个有序链表
        def merge(node1, node2):
            head = ListNode()
            dummy = head
            while node1 and node2:
                if node1.val < node2.val:
                    dummy.next = node1
                    node1 = node1.next
                else:
                    dummy.next = node2
                    node2 = node2.next
                dummy = dummy.next
            if node1:
                dummy.next = node1
            elif node2:
                dummy.next = node2
            return head.next

        dummy = ListNode()
        dummy.next = head
        # 获取链表长度
        count = 0
        while head:
            head = head.next
            count += 1

        intv = 1
        while intv < count:
            pre, cur = dummy, dummy.next

            while cur:
                head1 = cur
                # 为了把head1链表断开，cur必须是head1链表的最后一个节点
                for i in range(1, intv):
                    if cur.next:
                        cur = cur.next
                    else:
                        break
                # head2节点是head1链表的后面一个节点
                # head2可能为空
                head2 = cur.next
                cur.next = None
                cur = head2
                # cur移动到head2链表的最后一个节点
                for i in range(1, intv):
                    # 这里的判断条件需要考虑head2为空的情况
                    if cur and cur.next:
                        cur = cur.next
                    else:
                        break

                # temp保存head2链表后面一个节点
                # 如果head2为空的话，temp也为空
                temp = None
                if cur:
                    temp = cur.next
                    cur.next = None

                # merged是合并后的有序链表的头节点
                merged = merge(head1, head2)
                # 有序链表的头节点连到pre后面
                pre.next = merged
                # 更新pre的位置
                while pre.next:
                    pre = pre.next

                # 更新cur的位置，继续进行合并
                cur = temp
            intv <<= 1
        return dummy.next


if __name__ == '__main__':
    nodes = [4, 2, 3]
    for i in range(len(nodes)):
        if i == 0:
            head = ListNode(nodes[i])
            dummy = head
        else:
            head.next = ListNode(nodes[i])
            head = head.next
    x = Solution().sortList2(dummy)
    while x:
        print(x.val, end=' -> ')
        x = x.next
