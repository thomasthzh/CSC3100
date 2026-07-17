from collections import deque

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
n, m = map(int, input().strip().split())
grid = [list(input().strip()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
components = 0

sx = sy = tx = ty = -1
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            sx, sy = i, j
        elif grid[i][j] == 'T':
            tx, ty = i, j

#BFS
dist = [[-1]*m for _ in range(n)]
q = deque()
dist[sx][sy] = 0
q.append((sx, sy))
while q:
    x, y = q.popleft()
    if (x, y) == (tx, ty):
        break
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#' and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
shortest = dist[tx][ty]

#count
for i in range(n):
    for j in range(m):
        if grid[i][j] != '#' and not visited[i][j]:
            components += 1
            q2 = deque()
            q2.append((i, j))
            visited[i][j] = True
            while q2:
                x, y = q2.popleft()
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != '#':
                        visited[nx][ny] = True
                        q2.append((nx, ny))

print(shortest, components)