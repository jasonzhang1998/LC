# 任务调度器
import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)

        # 最多的执行次数
        maxExec = max(freq.values())
        # 具有最多执行次数的任务数量
        maxCount = sum(1 for v in freq.values() if v == maxExec)

        return max((maxExec - 1) * (n + 1) + maxCount, len(tasks))
