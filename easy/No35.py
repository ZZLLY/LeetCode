class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        # 题意: 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置
        # 限制: 数组中无重复元素
        # 思路: 二分查找
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left if nums[left] >= target else left+1

