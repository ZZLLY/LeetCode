class Solution:
    def generate(self, numRows: int) -> list:
        # 题意: 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
        # 思路: 模拟, 注意边界即可(如每层的第一个和最后一个数固定为1, 第一层和第二层单独处理, 以免越界)
        res = []
        for i in range(numRows):
            tmp = [1 for _ in range(i+1)]
            if i >= 2:
                for j in range(1, len(tmp)-1):
                    tmp[j] = res[i-1][j] + res[i-1][j-1]
            res.append(tmp)
        return res

s = Solution()
print(s.generate(5))