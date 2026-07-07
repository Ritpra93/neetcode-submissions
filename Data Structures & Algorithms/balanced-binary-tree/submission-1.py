# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #using iterative dfs
        #remember it's not just root balanced, but whole tree balanced
        stack = []
        node = root
        last = None
        depths = {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
                #traverse the left
            else:
                node = stack[-1]
                #LIFO, so get node from back
                if not node.right or last == node.right:
                    stack.pop()
                    left = depths.get(node.left, 0)
                    right = depths.get(node.right, 0)
                    if abs(left - right) > 1:
                        #check if count total is the same
                        return False
                    depths[node] = 1 + max(left, right)
                    #each gets counted
                    last = node
                    node = None   
                else:
                   node = node.right
                   #now traverse the right
        return True




    
        