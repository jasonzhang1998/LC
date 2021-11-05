# 合并k个升序链表


# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 把列表转换成链表节点
def listToNode(nodes):
    if not nodes:
        return
    head = None
    for value in nodes:
        if not head:
            head = ListNode(value)
            dummy = head
        else:
            head.next = ListNode(value)
            head = head.next
    return dummy


class Solution:
    # 递归地合并链表
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        # 剔除列表中空节点
        lists = [x for x in lists if x]
        n = len(lists)

        # lists为空说明所有排序完毕，直接返回
        if n < 1:
            return

        # dummy用于合并，head记录头结点，用于返回
        dummy = head = None
        while len(lists) == n:
            # 找出最小的节点，从其开始合并
            count = 0
            for i in range(n):
                if lists[i].val < lists[count].val:
                    count = i

            # 合并过程
            if not dummy:
                dummy = lists[count]

                # head记录头结点用于返回
                head = dummy
            else:
                # 每次最小的节点都接在dummy后面
                dummy.next = lists[count]
                dummy = dummy.next
            # 节点被合并之后要后移
            lists[count] = lists[count].next
            # 如果有一条链表到底了，即合并结束，跳出循环
            if not lists[count]:
                break
        # 合并剩余的列表
        dummy.next = self.mergeKLists(lists)
        return head


if __name__ == '__main__':
    lists = []
    nodes = [[0, 1, 2], [-10, -8, -5, -4], [], [], [-3], [-10, -9, -6, -4, -3, -2, -2, -1, 2], [-9, -9, -2, -1, 0, 1],
             [-9, -4, -3, -2, 2, 2, 3, 3, 4]]
    for node in nodes:
        lists.append(listToNode(node))
    x = Solution().mergeKLists(lists)
    while x:
        print(x.val, end="->")
        x = x.next
