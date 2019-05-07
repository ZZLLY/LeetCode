class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 题意: 给定两个二进制字符串，返回他们的和（用二进制表示）。
        # 限制: 输入为非空字符串且只包含数字 1 和 0。
        # 思路: 从后遍历模拟二进制加法
        # 技巧: 设定a,b的大小关系, 对位数不足的补0, 用-i的遍历方式可让a,b,res遍历项处于同一位置
        tmp = 0
        (a, b) = (a, b) if len(a) > len(b) else (b, a)
        b = '0'*(len(a)-len(b)) + b
        res = [0 for _ in range(len(a)+1)]
        for i in range(1, len(a)+1):
            res[-i] = int(a[-i]) + int(b[-i]) + tmp
            if res[-i] >= 2:
                tmp = 1
                res[-i] = res[-i] - 2
            else:
                tmp = 0
        res[0] = tmp
        return ''.join([str(c) for c in res]) if res[0] == 1 else ''.join([str(c) for c in res[1:]])

s = Solution()
print(s.addBinary("1011", "1010"))