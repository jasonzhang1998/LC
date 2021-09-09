# 两两交换链表中的节点

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre = ListNode(next=head)
        cur = head
        post = cur.next
        count = 0
        # 链表节点为单数时，最后一个节点不用翻转
        while cur and post:
            # 如果是最后两个节点，需要把交换后的尾节点的next置为空
            if not post.next:
                pre.next = post
                cur.next = None
                post.next = cur
                # 链表只有两个节点，head指向交换后的头结点
                if count == 0:
                    head = post
                break

            #  交换节点
            pre.next = post
            cur.next = post.next
            post.next = cur

            # head指向第一次交换后的头结点
            if count == 0:
                head = post

            # 指针向后更新
            pre = cur
            cur = pre.next
            post = cur.next
            count += 1
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    x = Solution().swapPairs(head)
    while x:
        print(x.val)
        x = x.next
