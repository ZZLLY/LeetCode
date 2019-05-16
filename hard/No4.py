class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        # 题意: 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
        # 限制: 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
        #       你可以假设 nums1 和 nums2 不会同时为空。
        # 思路: 用双指针指向两个数组
        #       如果有数组num1: [a1,a2,a3,...an]，nums2: [b1,b2,b3,...bn]
        #       那么[nums1[:left1],nums2[:left2] | nums1[left1:], nums2[left2:]]
        #       只要保证左右两个元素个数相同, 中位数就在|这个边界的旁边产生
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
        k = (n1 + n2 + 1) // 2
        left = 0
        right = n1
        # 用二分法找边界
        while left < right:
            m1 = left + (right - left) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2-1]:
                left = m1 + 1
            else:
                right = m1
        # 找到边界
        m1 = left
        m2 = k - m1
        c1 = max(nums1[m1 - 1] if m1 > 0 else float("-inf"), nums2[m2 - 1] if m2 > 0 else float("-inf"))
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 < n2 else float("inf"))
        return (c1 + c2) / 2