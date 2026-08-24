class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #not dfs, mininum number of minutes
        #level by level traversal 
        #store in queue like bfs
        #horizontally or vertically adjacent to rotten fruit = also rotten fruit
        #you need to all rotten oranges so this doesn't work the same way
        #neetcodes video says 4 directionally adjacent??, is that the same
        #could be multiple rotten oranges, don't use dfs because of this
        #initialize queue, add rotten oranges and pop through
        #each layer is our time lol
        #popleft since we want most recent, adding to the right, popping from left

        rows, cols = len(grid), len(grid[0])
        visited = set()
        #need a queue since bfs, since layer by layer, deque since adding and removing and can be done in O(1) time
        queue = deque()
        time = 0 
        freshOranges = 0
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        for r in range(rows):
            for c in range(cols):
                #1 represents a fresh fruit
                if grid[r][c] == 1:
                    freshOranges += 1
        while freshOranges > 0:
            #we know we can keep iterating since there is still fresh oranges
            is_rotten = False
            for r in range(rows):
                for c in range(cols):
                    #rotten fruit
                    if grid[r][c] == 2:
                        #go through all the different directions
                        for dr, dc in directions:
                            row, col = r + dr, c + dc
                            #bounds checking
                            if (row in range(rows) and 
                                col in range(cols) and 
                                grid[row][col] == 1):  

                                grid[row][col] = 3

                                #3 as a holder to check later for freshness and then to mark as rotten, since it goes 0, 1, 2
                                freshOranges -= 1
                                is_rotten = True
            if not is_rotten:
                return -1
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 3:
                        grid[r][c] = 2
        #we know there is still fresh oranges
            time += 1
        return time
    








        