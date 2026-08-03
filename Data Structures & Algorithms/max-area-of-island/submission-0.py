class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #use dfs for this, on every island
        #keep track of all grids that 0's vs 1's 
        #can move right left up down -> no diagonal
        #we'll need a visited set like most graph problems
        rows, columns = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if (r < 0 or c < 0 or r == rows or
              c == columns or grid[r][c] == 0 or (r,c) in visited):
              #cases to stop
                    return 0 
            visited.add((r,c))
             #this is for each of the directions, incrementing by one
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
             #go through everything now lol
        area = 0
        for r in range(rows):
            for c in range(columns):
                    area = max(area, dfs(r,c))
        return area
           
#these we can skip, or now we've explored everything posible
 #mark the zero rows as visited 
            #now regular 1 case



'''
In DFS:
If the cell is out of bounds or is '0', return.
Mark the current cell as '0' (visited).
Recursively explore all 4 directions (up, down, left, right).
Continue until all cells are processed.
Return the total island count.
'''