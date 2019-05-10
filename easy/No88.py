class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 题意: 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
        # 说明： 1、初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
        #       2、你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
        # 思路: 1、插入排序
        # if not nums2 or not nums1:
        #     return
        # i, index = 0, 0
        # while i < m and index < n:
        #     if nums1[i] > nums2[index]:
        #         for j in range(m-1, i-1, -1):
        #             nums1[j+1] = nums1[j]
        #         nums1[i] = nums2[index]
        #         index += 1
        #         m += 1
        #     i += 1
        # if index == n:
        #     return
        # else:
        #     length = len(nums1)
        #     for i in range(m, length):
        #         nums1[i] = nums2[index]
        #         index += 1

        #      2、归并排序的合并操作
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[i + j + 1] = nums2[j]
                j -= 1
            else:
                nums1[i + j + 1] = nums1[i]
                i -= 1
        if j >= 0:
            nums1[0:j + 1] = nums2[0:j + 1]



s = Solution()
s.merge([1,2,3,4,5,0], 5, [2], 1)