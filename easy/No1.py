class Solution:
    def twoSum(self, nums: list, target: int)->list:
        # 题意： 找到数组中两个整数之和为target, 返回他们的坐标
        # 限制： 一个整数只能用一次
        # 思路： 用字典, 遍历过程中, 每遍历到一个整数item, 把target-item当做key, 下标当做value, 在后续遍历的时候判断item是不是字典的key
        tmp = dict()
        for i in range(len(nums)):
            # 判断当前item是不是字典的key
            if tmp.__contains__(nums[i]):
                return [tmp[nums[i]], i]
            # 把target-nums[i]当做key放入字典, value是其下标
            tmp[target-nums[i]] = i
        return []

s = Solution()
print(s.twoSum([1,2,3],4))