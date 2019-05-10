# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 题意: 给定一个二叉树，检查它是否是镜像对称的。
        # 限制: 使用递归和迭代两种方法
        # 思路: 1.递归: 递归判断两个树是否相同：
        #             具体是查看左子树的左(右)子树与右子树的右(左)子树是否相同
        def check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return check(node1.left, node2.right) and check(node1.right, node2.left)
        if not root:
            return True
        if not root.left or not root.right:
            if not root.left and not root.right:
                return True
            else:
                return False
        return check(root.left, root.right)

    def isSymmetric2(self, root: TreeNode) -> bool:
        # 题意: 给定一个二叉树，检查它是否是镜像对称的。
        # 限制: 使用递归和迭代两种方法
        # 思路: 2.迭代: 层次遍历，检查每一层是否回文
        queue = [root]
        while queue:
            next_queue = []
            layer = []
            for node in queue:
                if not node:
                    layer.append(None)
                else:
                    layer.append(node.val)
                    next_queue.append(node.left)
                    next_queue.append(node.right)
            if layer != layer[::-1]:
                return False
            queue = next_queue
        return True







import time
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(2)
s = Solution()
start = time.clock()
for i in range(100000):
    s.isSymmetric(p)
end = time.clock()
print(end-start)

start = time.clock()
for i in range(100000):
    s.isSymmetric2(p)
end = time.clock()
print(end-start)
