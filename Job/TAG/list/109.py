# 有序链表转换二叉搜索树

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归分治法，每次快慢指针取中点，然后递归构造树
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return head
        if not head.next:
            return TreeNode(head.val)
        dummy = ListNode(next=head)
        slow, fast = dummy, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # node为链表的中间节点，即二叉搜索树的根节点
        node = slow.next
        pos = node.next
        slow.next = node.next = None
        root = TreeNode(node.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(pos)
        return root

    def sortedListToBST2(self, head: ListNode) -> TreeNode:
        def buildTree(left, right):
            if left > right:
                return
            # 根节点选择中间靠后的那个节点
            mid = (left + right + 1) // 2
            root = TreeNode()
            root.left = buildTree(left, mid - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = buildTree(mid + 1, right)
            return root

        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return buildTree(0, count - 1)
