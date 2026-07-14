# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0
            #in case root or node is null
            result = 0
            if node.val >= maxVal:
                result += 1
                #increment
            else:
                result += 0
                #no increment
            maxVal = max(maxVal, node.val)
            #keep track of max
            result += dfs(node.left, maxVal)
            #go left side
            result += dfs(node.right, maxVal)
            #go right side
            return result
        return dfs(root, root.val)
        
        