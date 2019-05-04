class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        # 题意： 查找字符串数组的最长公共前缀
        # 限制： 如果不存在, 返回''; 所有输入只包含小写字母a-z
        # 思路： 用set和指针的性质遍历字符串数组
        if not strs:
            return ''
        index = 0
        for item in zip(*strs):
            if len(set(item)) != 1:
                break
            index += 1
        return strs[0][:index]

s = Solution()
print(s.longestCommonPrefix(["a"]))
