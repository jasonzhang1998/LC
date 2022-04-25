# 反转链表II

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 头插法，将left+1到right节点全部插到left-1节点后面
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(next=head)
        cur = dummy
        for _ in range(left - 1):
            cur = cur.next

        # pre为left节点的前一个节点，之后的节点都插到pre后面
        pre = cur
        cur = cur.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
        return dummy.next


nodes = [1, 2, 3, 4, 5]
dummy = ListNode()
cur = dummy
for num in nodes:
    node = ListNode(num)
    cur.next = node
    cur = cur.next

ans = Solution().reverseBetween(dummy.next, 2, 4)
while ans:
    print(ans.val)
    ans = ans.next
