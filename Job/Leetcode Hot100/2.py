# 两数相加


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 遍历列表，取出数，相加，再建表
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = num2 = i = 0
        while l1:
            num1 += l1.val * 10 ** i
            l1 = l1.next
            i += 1
        i = 0
        while l2:
            num2 += l2.val * 10 ** i
            l2 = l2.next
            i += 1
        numSum = num1 + num2
        if numSum == 0:
            return ListNode(0)
        tail = None
        while numSum > 0:
            num = numSum % 10
            if not tail:
                tail = ListNode(num)
                head = tail
            else:
                tail.next = ListNode(num)
                tail = tail.next
            numSum //= 10
        return head

    # 直接边遍历链表，边相加。用flag记录进位
    # 长度不一样的话，剩下的直接补后面，但要考虑进位
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        tail = None
        while l1 and l2:
            num = (l1.val + l2.val + flag) % 10
            if not tail:
                tail = ListNode(num)
                head = tail
            else:
                tail.next = ListNode(num)
                tail = tail.next
            flag = (l1.val + l2.val + flag) // 10
            l1 = l1.next
            l2 = l2.next

        if not l1:
            node = l2
        else:
            node = l1
        while node:
            num = (flag + node.val) % 10
            tail.next = ListNode(num)
            tail = tail.next
            flag = (flag + node.val) // 10
            node = node.next
        if flag:
            tail.next = ListNode(1)
        return head


if __name__ == '__main__':
    l1 = ListNode(3)
    l1.next = ListNode(7)
    # l1.next.next = ListNode(9)
    l2 = ListNode(9)
    l2.next = ListNode(2)
    # l2.next.next = ListNode(9)
    x = Solution().addTwoNumbers2(l1, l2)
    while x:
        print(x.val)
        x = x.next
