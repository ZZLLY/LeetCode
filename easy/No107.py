# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list:
        # 题意: 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
        # 思路: 两个队列非递归, 层序遍历, 用tmp记录一层的值, 再append到res, 返回时res反转
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            tmp = []
            next_queue = []
            for node in queue:
                tmp.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
            res.append(tmp)
        return res[::-1]
