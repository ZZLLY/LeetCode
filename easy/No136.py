class Solution:
    def singleNumber(self, nums: list) -> int:
        # 题意: 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
        # 限制: 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
        # 思路: 运用异或的特性, 0^n = n, n^n = 0
        res = 0
        for item in nums:
            res = res ^ item
        return res