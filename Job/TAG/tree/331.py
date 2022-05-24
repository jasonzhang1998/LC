# 验证二叉树的前序序列化

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        n = len(nodes)
        stack = [1]
        for i in range(n):
            if not stack:
                return False
            else:
                stack[-1] -= 1
                if stack[-1] == 0:
                    stack.pop()
            if nodes[i] != '#':
                stack.append(2)
        return not stack
    
    def isValidSerialization2(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        count = 1
        for i in range(len(nodes)):
            if count == 0:
                return False
            else:
                count -= 1
            if nodes[i] != '#':
                count += 2
        return count == 0

            

preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
print(Solution().isValidSerialization2(preorder))
