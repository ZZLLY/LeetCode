# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 题意: 给定一个二叉树，判断它是否是高度平衡的二叉树。
        # 限制: 本题中，一棵高度平衡二叉树定义为：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
        # 思路: 1、两重递归, 计算左右子树的深度, 判断是否符合, 再递归调用左右子树
        #        这种方法是比较繁琐的，有些步骤重复计算导致时间变慢
        # def max_depth(root):
        #     if not root:
        #         return 0
        #     left = max_depth(root.left)
        #     right = max_depth(root.right)
        #     return max(left, right)+1
        # if not root:
        #     return True
        # if abs(max_depth(root.left) - max_depth(root.right)) > 1:
        #     return False
        # return self.isBalanced(root.left) and self.isBalanced(root.right)
        #     2、可以想到, 不用从上至下判断整个左右子树的深度,
        #        因为左右子树的深度是同时计算的, 那么一旦出现左右子树不平衡, 就可立即返回, 结束递归
        def balance(root):
            if not root:
                return 0
            left = balance(root.left)
            if left == -1:
                return -1
            right = balance(root.right)
            if right == -1:
                return -1
            # 一旦出现不平衡返回-1, 不用等待子树递归
            if abs(left - right) > 1:
                return -1
            return left+1 if left > right else right+1
        return balance(root) != -1

