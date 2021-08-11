# 翻转链表的倒数第N个节点


# 定义链表类
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 快慢指针法，先让快指针走N + 1步，然后快慢指针一起走，最后慢指针指向待删除节点的前驱节点
# 第一个重点：快慢指针相差N + 1步，方便进行删除操作
# 第二个重点：由于需要对头节点进行删除操作，因此需要新建一个虚拟头节点dummy，用于删除头节点
# 第三个重点：最后的返回值是dummy.next，而不是head，因为head有可能会被删除
def removeNthFromEnd(head, n):
    dummy = ListNode(next=head)
    fast = dummy
    slow = dummy
    for i in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head = removeNthFromEnd(head, 1)
    while head:
        print(head.val)
        head = head.next

