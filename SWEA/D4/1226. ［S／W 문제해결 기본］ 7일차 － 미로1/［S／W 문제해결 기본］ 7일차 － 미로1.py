from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    if maze[r][c] == 3:
        return True
    visited[r][c] = True
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0<= nr < 16 and 0 <= nc < 16 and maze[nr][nc] != 1 and not visited[nr][nc]:
            if dfs(nr, nc):
                return 1
            
    return 0
    

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    result = dfs(1, 1)
    print(f'#{tc} {result}')
    
