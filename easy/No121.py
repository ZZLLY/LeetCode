class Solution:
    def maxProfit(self, prices: list) -> int:
        # 题意: 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
        #      如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
        # 限制: 注意你不能在买入股票前卖出股票。
        # 思路: 动态规划, 记录最小值和序列后的最大差价
        if not prices:
            return 0
        max_p, min_p = 0, prices[0]
        for item in prices:
            min_p = min(min_p, item)
            max_p = max(max_p, item - min_p)
        return max_p


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))