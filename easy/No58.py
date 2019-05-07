class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 题意: 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
        #      如果不存在最后一个单词，请返回 0 。
        # 限制：一个单词是指由字母组成，但不包含任何空格的字符串。
        # 思路:从后遍历, 遇到空格需要分两种情况, 1.若之前遇到过非空格, break 2.若之前没遇到非空格, continue
        length = len(s)
        count = 0
        for i in range(length-1, -1, -1):
            if s[i] == ' ':
                if count > 0:
                    break
                else:
                    continue
            else:
                count += 1
        return count