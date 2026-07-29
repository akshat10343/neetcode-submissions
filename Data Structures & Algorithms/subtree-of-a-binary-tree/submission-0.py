# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        elif root.val == subRoot.val:
            if self.helper(root,subRoot) == True:
                return True

        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left, subRoot)
    def helper(self,q: Optional[TreeNode], p: Optional[TreeNode]) -> bool:
        if (p is None) and (q is None):
            return True
        elif p is None or q is None:
            return False
        return self.helper(p.left, q.left) and self.helper(p.right, q.right) and p.val == q.val
