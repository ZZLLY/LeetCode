class Solution:
    def maxSubArray(self, nums: list) -> int:
        # 题意: 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
        # 思路: 动规, 记录当前解, 如果该解大于零, 则有向后传递的价值, 否则不如从0开始
        length = len(nums)
        for i in range(1, length):
            nums[i] = nums[i] + max(nums[i-1], 0)
        return max(nums)
