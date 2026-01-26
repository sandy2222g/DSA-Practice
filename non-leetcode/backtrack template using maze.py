def maze_backtracking(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    res = []
    visited = [[False] * cols for _ in range(rows)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(r, c, path):
        # validity
        if (
            r < 0 or c < 0 or
            r >= rows or c >= cols or
            maze[r][c] == 0 or
            visited[r][c]
        ):
            return

        # base case
        if (r, c) == end:
            res.append(path + [(r, c)])
            return

        
        visited[r][c] = True
        path.append((r, c))

        # explore
        for dr, dc in directions:
            dfs(r + dr, c + dc, path)

        # exclude backtrack 
        path.pop()
        visited[r][c] = False

    dfs(start[0], start[1], [])
    return res


# Example
maze = [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]
]

start = (0, 0)
end = (2, 2)

paths = maze_backtracking(maze, start, end)
print(paths)
