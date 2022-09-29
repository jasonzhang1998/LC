import queue
from typing import List
class Solution:
    # 水壶问题
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        seen = set()
        q = queue.deque()
        q.append((0, 0))
        while q:
            x, y = q.popleft()
            if x == targetCapacity or y == targetCapacity or x + y == targetCapacity:
                return True
            if (x, y) in seen:
                continue
            seen.add((x, y))
            q.append((jug1Capacity, y))
            q.append((0, y))
            q.append((x, jug2Capacity))
            q.append((x, 0))
            if x > jug2Capacity - y:
                q.append((x + y - jug2Capacity, jug2Capacity))
            else:
                q.append((0, x + y))
            if y > jug1Capacity - x:
                q.append((jug1Capacity, x + y - jug1Capacity))
            else:
                q.append((x + y, 0))
        return False

    # 24点游戏(diy版)
    def judgePoint24(self, cards: List[int]) -> bool:

        # 生成所有排列
        def dfs(index):
            if index == 4:
                permutation.append(cards[:])
                return
            # index表示交换的起点
            for i in range(index, 4):
                cards[i], cards[index] = cards[index], cards[i]
                dfs(index + 1)
                cards[i], cards[index] = cards[index], cards[i]
        # 根据数字排列，组合出所有表达式
        def getString(nums):
            chars = [''] * 7
            for i in range(4):
                chars[2 * i] = str(nums[i])
            icons = ['+', '-', '*', '/']
            expre = []
            def help(index):
                if index == 3:
                    expre.append(''.join(chars))
                    return
                for i in range(4):
                    chars[2 * index + 1] = icons[i]
                    help(index + 1)
            help(0)
            
            # 添加括号
            ans = []
            for string in expre:
                # 加一个括号
                ans.append('(' + string[:3] + ')' + string[3:])
                ans.append(string[:2] + '(' + string[2:5] + ')' + string[5:])
                ans.append(string[:4] + '(' + string[4:] + ')')
                ans.append(string[:2] + '(' + string[2:] + ')')
                ans.append('(' + string[:5] + ')' + string[5:])
                # 加两个括号
                ans.append('(' + string[:3] + ')' + string[3] + '(' + string[4:] + ')')
                ans.append('(' + '(' + string[:3] + ')' + string[3:5] + ')' + string[5:])
                ans.append('(' + string[:2] + '(' + string[2:5] + ')' + ')' + string[5:])
                ans.append(string[:2] + '(' + '(' + string[2:5] + ')' + string[5:] + ')')
                ans.append(string[:2] + '(' + string[2:4] + '(' + string[4:] + ')' + ')')
            return ans
        permutation = []
        dfs(0)
        for card in permutation:
            expres = getString(card)
            for expre in expres:
                try:
                    answer = eval(expre)
                except:
                    continue
                if abs(answer - 24) < 1e-6:
                    # print(expre, answer)
                    return True
        return False

