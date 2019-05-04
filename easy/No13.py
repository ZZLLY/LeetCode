class Solution:
    def romanToInt(self, s: str) -> int:
        # 题意： 按照指定规则, 推出罗马数字对应的阿拉伯数字
        # 限制： 通常情况下，罗马数字中小的数字在大的数字的右边. 但也有特殊情况, 如IV表示5-1=4
        # 思路： 用字典存储罗马数字, 根据特殊情况, 两两结合起来判断
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)-1):
            if dict[s[i]] < dict[s[i+1]]:
                res -= dict[s[i]]
            else:
                res += dict[s[i]]
        res += dict[s[-1]]
        return res