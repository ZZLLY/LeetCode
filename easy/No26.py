class Solution:
    def removeDuplicates(self, nums: list) -> int:
        # 题意: 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
        # 限制: 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
        # 思路: 用一个游标和一个记录首次不同元素的空间
        if len(nums) <= 1:
            return len(nums)
        index = 1
        length = len(nums)
        left_num = nums[0]
        for i in range(1, length):
            if nums[i] != left_num:
                nums[index] = nums[i]
                left_num = nums[i]
                index += 1
        return index