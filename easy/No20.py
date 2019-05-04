class Solution:
    def isValid(self, s: str) -> bool:
        # 题意： 给定一个只包括 '(',')','{','}','[',']' 的字符串,判断字符串是否有效
        # 限制： 有效字符串需满足：
        #       1.左括号必须用相同类型的右括号闭合。
        #       2.左括号必须以正确的顺序闭合。
        # 思路： 用栈的性质, 如果当前与top-1的元素匹配top = top-1, 不匹配return False, 最后查看top是否为原值
        # 注意：top初始值为1, 预留一位防止top-1越界
        if not s:
            return True
        stack = [' ' for _ in range(len(s) + 1)]
        top = 1
        for c in s:
            if c in ['(', '[', '{']:
                stack[top] = c
                top += 1
            elif c == ')' and stack[top - 1] != '(':
                return False
            elif c == ']' and stack[top - 1] != '[':
                return False
            elif c == '}' and stack[top - 1] != '{':
                return False
            else:
                top -= 1
        return top == 1

s = Solution()
print(s.isValid("([)]"))
