class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #3 different cases
        #use dfs like other graph problems?
        #check if each cell is inf and if it is run dfs
        #all 4 directions min(1+ dfs(neighbor))
        #brute force below
        '''
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0, 1), (0, -1)]
        INF = 2147483647
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or
                c >= cols or grid[r][c] == -1 or visited[r][c]):
                    return INF
            if grid[r][c] == 0:
                return 0 
                
            visited[r][c] = True
            res = INF 
            for dx, dy in directions:
                #trying all 4 directions in both rows and columns 
                res = min(res, 1 + dfs(r + dx, c + dy))
            visited[r][c] = False
            return res
             
            #go through all of the options, backtracking and if inf use dfs
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == INF:
                    grid[r][c] = dfs(r,c)
                '''
        #non brute force uses bfs
        #use bfs on all treasures
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        #directions = [(1,0), (-1,0), (0, 1), (0, -1)]
        #won't need directions since incrementing each one
        visited = set()
        q = deque()
        def AddTreasureCells(r, c):
            
            if(min(r, c) < 0 or r == rows or c == cols or (r, c) in     visited or grid[r][c] == -1):
                #not in bounds
                return 
            visited.add((r,c))
            q.append([r, c])
            #add to queue 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
                    #add as visited
        dist = 0
        # to track distance to nearest trasure
        #actual bfs part
        while q:
            for i in range(len(q)):
                #process each node, and try each of the nearest directions for that level
                r, c = q.popleft()
                grid[r][c] = dist
                AddTreasureCells(r+1, c)
                AddTreasureCells(r-1, c)
                AddTreasureCells(r, c+1)
                AddTreasureCells(r, c-1)
            dist += 1
            #increase distance to go to next level
                

                
    
             
        