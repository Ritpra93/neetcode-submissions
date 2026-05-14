# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        small = min(p.val, q.val)
        large = max(p.val, q.val)
        while root:
            if root.val > large:
                root = root.left #p,q belong to left subtree. since the values of p val and q val less than root
            elif root.val < small:
                root = root.right #p,q belong to right subtree, same idea as basically before
            else:
                return root #case where its in between
        return None

        