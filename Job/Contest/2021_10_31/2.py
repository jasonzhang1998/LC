# 找出临界点之间的最小和最大距离


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 其实不用先遍历一遍链表把他们放到列表里，可以直接用三个指针遍历，进行优化
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        n = len(ls)
        tmp = []
        first = 0
        minDis = len(ls)
        for i in range(1, n - 1):
            if (ls[i] > ls[i - 1] and ls[i] > ls[i + 1]) or (ls[i] < ls[i - 1] and ls[i] < ls[i + 1]):
                if not tmp:
                    first = i
                else:
                    if i - tmp[-1] < minDis:
                        minDis = i - tmp[-1]
                tmp.append(i)
        print(tmp)
        if len(tmp) < 2:
            return [-1, -1]
        maxDis = tmp[-1] - tmp[0]

        return [minDis, maxDis]
