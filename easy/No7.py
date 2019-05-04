class Solution:
    def reverse(self, x: int)-> int:
        # 题意： 给出一个32位带符号整数, 将这个整数反转
        # 限制： 如果反转后的整数超出[-2^31, 2^31-1], 返回0
        # 思路： 根据数学性质, 灵活使用取余和除的操作即可
        # 注意： python里//是向下取整, 对负数来说, -0.5这样的数会取为-1, 所以要分类讨论
        res = 0
        # 用一个flag记录x的正负性
        flag = 1 if x > 0 else 0
        x = abs(x)
        while x:
            res = res*10 + x%10
            x = x // 10
        if not flag:
            res = -res
        return res if -2**31 <= res <= 2**31-1 else 0

s = Solution()
print(s.reverse(1563847412))