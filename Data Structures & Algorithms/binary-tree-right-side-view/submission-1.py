# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        check = []
        self.helper(root,0, check)
        check2 = []
        for i in check:
            check2.append(i[-1])
        return (check2)
        
    def helper(self, node, depth, res):
        if node is None:
            return
        if depth == len(res):
            res.append([])
        res[depth].append(node.val)
        self.helper(node.left, depth + 1, res)
        self.helper(node.right, depth + 1, res)

