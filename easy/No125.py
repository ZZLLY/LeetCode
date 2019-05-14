class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 题意: 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
        # 限制: 空字符串定义为有效的回文串。
        # 思路: 1、原始的方法, 根据ascii码的大小筛选出数字和字母(大写转小写)
        if not s:
            return True
        res = ''
        for c in s:
            if 'a' <= c <= 'z' or '0' <= c <= '9':
                res += c
            elif 'A' <= c <= 'Z':
                res += chr(ord(c)+32)
        return res == res[::-1]

        #    2、用过滤器+str.isalnum筛选出数字和字母, 再用.lower()转成小写
        # if not s:
        #     return True
        # res = ''.join(filter(str.isalnum, s)).lower()
        # return res == res[::-1]

s = Solution()
print(s.isPalindrome('0P'))
