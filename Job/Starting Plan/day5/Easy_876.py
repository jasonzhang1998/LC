# 链表的中间的结点


# 定义链表类
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 使用快慢指针，快指针每次走两步，慢指针每次走一步，快指针到达终点时，慢指针指向中间结点
def middleNode(head):
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(middleNode(head))

