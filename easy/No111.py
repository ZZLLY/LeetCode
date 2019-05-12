# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 题意: 给定一个二叉树，找出其最小深度。
        #       最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
        # 思路: 递归,
        #       如果左右子树都存在, 递归左右子树,
        #       如果只有一个子树存在, 向下递归那个子树,
        #       如果没有子树, 说明是叶子节点, 可以返回1结束递归
        if not root:
            return 0
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        elif root.left:
            return 1 + self.minDepth(root.left)
        elif root.right:
            return 1 + self.minDepth(root.right)
        else:
            return 1
