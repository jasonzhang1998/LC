# 两数之和
# 两次遍历或者使用哈希表一次遍历
def sum(nums, target):
    # hashtable = dict()
    hashtable = {}
    for i, num in enumerate(nums):
        if (target - num) in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 10]
    target = 18
    print(sum(nums, target))
    print('hello')
