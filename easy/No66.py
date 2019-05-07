class Solution:
    def plusOne(self, digits: list) -> list:
        # 题意:给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
        #     最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
        #     你可以假设除了整数 0 之外，这个整数不会以零开头
        # 思路:从后往前遍历, 用tmp记录进位, 如果进位溢出, 即tmp==1, 返回[1]+digits
        length = len(digits)
        tmp = 1
        for i in range(length-1, -1, -1):
            digits[i] += tmp
            if digits[i] >= 10:
                tmp = 1
                digits[i] -= 10
            else:
                tmp = 0
                break
        return digits if tmp == 0 else [1]+digits