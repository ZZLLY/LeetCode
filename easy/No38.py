class Solution:
    def countAndSay(self, n: int) -> str:
        # 题意: 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数
        # 思路: 根据规则模拟即可
        str1 = '1'
        for _ in range(n-1):
            length = len(str1)
            str2 = ''
            count = 1
            for i in range(1, length):
                if str1[i] != str1[i-1]:
                    str2 += str(count) + str1[i-1]
                    count = 1
                else:
                    count += 1
            str2 += str(count) + str1[length-1]
            str1 = str2
        return str1

