# m 2m
#
# a + nb + x = m
# a + kb + x = 2m
# m = (k - n)b
# a + x = (k - 2*n)b
class ListNode:
    def __int__(self, val):
        self.val = val
        self.next = None


def cycleList(head):
    slow = fast = head
    flag = False
    while fast:
        if fast.next:
            fast = fast.next.next
        slow = slow.next
        if fast == slow:
            flag = True
            break
    if not flag:
        return
    temp = head
    while temp != slow:
        temp, slow = temp.next, slow.next
    entry = slow
    count = 1
    slow = slow.next
    while slow != entry:
        slow = slow.next
        count += 1
    return entry, count


if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5, 6, 7]
    head = ListNode()
    cur = head
    for node in nodes:
        cur.next = ListNode()
        cur.next.val = node
        cur = cur.next
    # 环入口是3，长度为5
    cur.next = head.next.next.next
    node, length = cycleList(head.next)
    print(node.val, length)
