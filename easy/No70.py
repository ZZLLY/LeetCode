class Solution:
    def climbStairs(self, n: int) -> int:
        # 题意: 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
        # 限制: 给定n是一个正整数
        # 思路: 斐波那契数列, 用动规
        if n <= 2:
            return n
        a = 1
        b = 2
        for _ in range(2, n):
            a, b = b, (a+b)
        return b

s = Solution()
print(s.climbStairs(3))