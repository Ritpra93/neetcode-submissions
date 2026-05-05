# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
      #add both root and val
        while stack:
            cur, val = stack.pop()
            #current node and val

            if not cur.left and not cur.right and val == targetSum:
                    return True
                #case where you've found targetSum, remember you can have neg values
            if cur.right:
                stack.append((cur.right, val+cur.right.val))
            if cur.left:
                stack.append((cur.left, val+cur.left.val))
                #double parantheses for a stack, tuple
        return False
        