# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 题意: 给定一个二叉树，找出其最大深度。
        # 思路: 1、递归查找左右子树, DFS+分治, 简洁但耗时长
        # return 0 if not root else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        #      2、两个队列非递归，层序遍历记录最大深度
        if not root:
            return 0
        queue = [root]
        count = 0
        while queue:
            count += 1
            next_queue = []
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        return count