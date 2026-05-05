# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack =[(root, False)]
        max_height_dict = {} #keep a dictionary for all the different heights
        #root visited since added to stack
        diameter = 0
        while stack:
            node, visited = stack.pop()
            #as always for stacks/dfs pop first
            if not visited:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                    #visited
                if node.right:
                    stack.append((node.right, False))
            else:
                if node.left is None:
                    left_height = 0
                else:
                    left_height = max_height_dict.pop(node.left)
                if node.right is None:
                    right_height = 0
                else:
                    right_height = max_height_dict.pop(node.right)
                
                diameter = max(diameter, left_height + right_height)
                max_height_dict[node] = max(left_height, right_height) + 1
        return diameter
        
            
            


        