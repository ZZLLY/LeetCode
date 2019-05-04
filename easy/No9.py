class Solution:
    def isPalindrome(self, x: int)-> bool:
        # 题意： 判断一个整数是不是回文数
        # 限制： 不转化为字符串来解决
        # 思路： 首先, 负数的‘-’决定了负数肯定不是回文数, 然后用%和//计算出反转数, 判断与原数是否相等即可
        if x<0:
            return False
        res = 0
        tmp_x = x
        while x:
            res = res*10 + x%10
            x = x // 10
        return tmp_x == res

s = Solution()
print(s.isPalindrome(121))