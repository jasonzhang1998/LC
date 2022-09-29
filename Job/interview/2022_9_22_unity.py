class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

def reSortList(head):
    # 反转链表
    def reverseList(node):
        if not node or not node.next:
            return node
        dummy = ListNode(next=node)
        pre = node
        cur = node.next
        while cur:
            pre.next = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = pre.next
        return dummy.next
    
    if not head or not head.next:
        return head
    # 切分链表
    slow, fast = head, head.next
    while fast:
        if fast.next:
            fast = fast.next.next
        else:
            break
        slow = slow.next
    
    new_head = slow.next
    slow.next = None
    # printList(new_head)
    reversed_head = reverseList(new_head)

    # printList(reversed_head)
    
    pre = head
    pos = reversed_head
    # printList(pre)
    # printList(pos)
    while pos:
        temp = pos.next
        pos.next = pre.next
        pre.next = pos
        pos = temp
        pre = pre.next.next
    # print('here')
    return head

def constructList(nums):
    nums.reverse()
    dummy = ListNode()
    for i in range(len(nums)):
        node = ListNode(nums[i])
        node.next = dummy.next
        dummy.next = node
    return dummy.next

def printList(head):
    if not head:
        return
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    print(ans)

values = [1,2,3,4,5] 
test_list = constructList(values)
printList(test_list)
new_list = reSortList(test_list)
printList(new_list)