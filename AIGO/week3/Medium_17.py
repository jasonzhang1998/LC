# 电话号码的字母组合


# 使用回溯法求所有电话号码的排列组合，回溯法的核心在于回溯函数，回溯函数模板如下：

'''
def backtrack(需要的参数):
    if 终止条件（往往是多叉树的叶子节点）：
        收集结果，将此条路径的结果存储到答案集中
        return

    for循环  遍历当前层数的所有节点：
        判断是否是一个合法的选择（本题不需要用到）
        执行这一层遍历所需做的操作
        backtrack(改变参数，进入下一层进行遍历)
        执行回溯操作（即将之前执行的操作进行回退）
'''


def letterCombinations(digits):
    if not digits:
        return []
    hashtable = {'2': "abc",
                 '3': "def",
                 '4': "ghi",
                 '5': "jkl",
                 '6': "mno",
                 '7': "pqrs",
                 '8': "tuv",
                 '9': "wxzy"}
    n = len(digits)

    def backtrack(index):
        if index == n:
            ans.append("".join(track))
            return
        letters = digits[index]
        for letter in hashtable[letters]:
            track.append(letter)
            backtrack(index + 1)
            track.pop()

    ans = []
    track = []
    backtrack(0)
    return ans


# 使用队列来进行排列组合
def letterCombinations2(digits):
    if not digits:
        return []
    # 可以通过ASCII码来找到字符和数字的关系，因此可以不用字典存放数字对应的字符串
    phone = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxzy"]
    queue = [''] # 初始化队列，里边放入一个空字符串，用于第一轮入队
    for digit in digits:
        for i in range(len(queue)):
            # 每次先将队头元素出队，然后与此时字符对应的字符串的各个字符拼接之后入队
            tmp = queue.pop(0)
            for letter in phone[ord(digit) - 50]:
                queue.append(tmp + letter)
    return queue


if __name__ == '__main__':
    digits = "678"
    print(letterCombinations2(digits))
    print(len(['']))
