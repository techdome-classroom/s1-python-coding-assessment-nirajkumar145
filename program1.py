class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r: int, c: int):
            # Base conditions to stop recursion
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W' or visited[r][c]:
                return
            # Mark the cell as visited
            visited[r][c] = True
            # Explore the four possible directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        island_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L' and not visited[r][c]:
                    # Start a new DFS to mark the whole island
                    dfs(r, c)
                    island_count += 1

        return island_count
         
