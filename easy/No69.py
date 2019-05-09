class Solution:
    def mySqrt(self, x: int)->int:
        # 题意: 计算并返回X的平方根, 其中x是非负整数
        # 限制: 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去
        # 思路: 1、比较好想到的就是二分查找
        #      2、牛顿迭代法快速寻找平方根, 原理是假定有f(r)=r^2-x这样一条曲线, 用(r, f(r))点上的切线与横轴的交点来不断逼近r^2-x=0的根.

        # way1
        # left = 0
        # right = x
        # mid = x // 2
        # while left <= right:
        #     if mid * mid > x:
        #         right = mid - 1
        #     elif mid * mid < x:
        #         left = mid + 1
        #     else:
        #         return mid
        #     mid = (left + right) // 2
        # return mid

        # way2
        if x <= 1:
            return x
        r = x
        while r > x/r:
            r = (r + x/r) // 2
        return int(r)


import time
s = Solution()
start = time.clock()
for _ in range(100000):
    s.mySqrt(8)
end = time.clock()
print('%s' % (end-start))
