# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 题意: 给定两个二叉树，编写一个函数来检验它们是否相同。
        #      如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
        # 思路: 用递归查看各个位置是否相同
        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        else:
            if not p and not q:
                return True
            else:
                return False


from copy import copy
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q = copy(p)
s = Solution()
print(s.isSameTree(p, q))