class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        # 题意: 给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
        # 限制: 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
        # 思路: 用一个游标
        index = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index