# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #bfs iterative solution, fifo
        res = []
        queue = collections.deque([root])
        while queue:
            right_side = None
            queue_len = len(queue)
            for i in range(queue_len):
                node = queue.popleft()
                #popleft in bfs due to fifo
                if node:
                    right_side = node
                    queue.append(node.left)
                    queue.append(node.right)
            if right_side:
                #gotta make sure not null
                res.append(right_side.val)
        return res
                
       


        