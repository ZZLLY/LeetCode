class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 题意: 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
        # 思路: 判断字符是否在tmp里, 如果不在就加进去, 如果已存在则截取出现字符的后半段
        if not s:
            return 0
        res = 0
        tmp = ''
        for c in s:
            if c not in tmp:
                tmp += c
            else:
                res = max(len(tmp), res)
                tmp = tmp.split(c)[1] + c
        res = max(len(tmp), res)
        return res

s = Solution()
print(s.lengthOfLongestSubstring('aab'))