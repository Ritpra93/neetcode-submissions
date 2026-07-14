# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root):
        #iterative solution
        stack = [(root, root.val)]
        #keep the root and it's value in stack
        count = 0
        #keep a count
        while stack:
            #like most dfs problems
            node, maxVal = stack.pop()
            #remember you have root and val in stack
            if node.val >= maxVal:
                count += 1
                #increment based on it being good
            newMax = max(maxVal, node.val)
            #keep max
            if node.left: stack.append((node.left, newMax))
            #go left first always and add nodes to stack
            if node.right: stack.append((node.right, newMax))
            #same with right
        return count
        #not u have count

        
        