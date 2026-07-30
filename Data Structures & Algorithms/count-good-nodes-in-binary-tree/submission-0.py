# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.helper(root, root.val)
        return self.count
        pass

    def helper(self, node, new_max):
        if node is None:
            return
        if node.val >= new_max:
            self.count += 1
            new_max = max(new_max, node.val)

        self.helper(node.right, new_max)
        self.helper(node.left, new_max)
        return self.count