1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        if not grid:
4            return 0
5
6        # Setup required ds
7        ROWS, COLS = len(grid), len(grid[0])
8        visit = set()
9        island_cnt = 0
10        
11        # helper
12        def bfs(r, c):
13            q = deque()
14            visit.add((r, c))
15            q.append((r, c))
16
17            while q:
18                row, col = q.pop()
19                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
20
21                for dr, dc in directions:
22                    r, c = row + dr, col + dc
23                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == '1' and (r, c) not in visit:
24                        q.append((r, c))
25                        visit.add((r, c))
26        
27        
28        for r in range(ROWS):
29            for c in range(COLS):
30                if grid[r][c] == '1' and (r, c) not in visit:
31                    bfs(r, c)
32                    island_cnt += 1
33        
34    
35        return island_cnt
36                