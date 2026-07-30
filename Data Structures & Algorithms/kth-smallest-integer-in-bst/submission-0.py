# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.l = []
        self.helper(root)
        #print(self.l)
        self.l = sorted(self.l)
        return self.l[k-1]

        pass

    def helper(self, node):
        if node is None:
            return None
        self.l.append(node.val)
        self.helper(node.right)
        self.helper(node.left)
