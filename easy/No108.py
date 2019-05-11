# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        # 题意: 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树
        # 限制: 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1
        # 思路: 递归, 输入为升序, 那最中间的节点当做root, 左右数组切片为左右子树, 再递归调用左右子树
        if not nums:
            return None
        mid = len(nums) >> 1
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
