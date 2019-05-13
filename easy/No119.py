class Solution:
    def getRow(self, rowIndex: int) -> list:
        # 题意: 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
        # 思路: 组合公式C(n,i) = n!/(i!*(n-i)!), 第(i+1)项是第i项的倍数=(n-i)/(i+1);
        res = []
        b = 1
        for i in range(rowIndex+1):
            res.append(b)
            b = b*(rowIndex-i)//(i+1)
        return res

s = Solution()
print(s.getRow(3))