# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 耍赖做法，先将链表读入列表，然后排序，最后用有序的数组新建链表，返回头结点
def sortList(head):
    if not head:
        return None
    res = []
    while head:
        res.append(head.val)
        head = head.next
    res.sort(reverse=True)
    for i in range(len(res)):
        if i == 0:
            dummy = ListNode(res[i])
        else:
            p = ListNode(res[i])
            p.next = dummy
            dummy = p
    return dummy


# 自顶向下归并排序
def sortList2(head):
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

    # 递归地切分链表
    def sortFunc(node):
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
        left = sortFunc(node)
        right = sortFunc(node1)
        return merge(left, right)

    return sortFunc(head)


if __name__ == '__main__':
    nums = [4, 1, 2, 3]
    # 尾插法，新结点每次都插在原链表尾结点后面
    for i in range(len(nums)):
        if i == 0:
            head = ListNode(nums[i])
            dummy = head
        else:
            dummy.next = ListNode(nums[i])
            dummy = dummy.next

    # 头插法，新结点每次插到原链表头结点前面
    # for i in range(len(nums)):
    #     if i == 0:
    #         head = ListNode(nums[i])
    #     else:
    #         p = ListNode(nums[i])
    #         p.next = head
    #         head = p

    head = sortList2(head)

    while head:
        print(head.val, end=" ")
        head = head.next
