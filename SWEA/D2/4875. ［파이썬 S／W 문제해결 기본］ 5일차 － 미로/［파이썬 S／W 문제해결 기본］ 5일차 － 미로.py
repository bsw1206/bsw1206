from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(start_r, start_c):
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0<= nr < N and 0<= nc < N and not visited[nr][nc]:
                if maze[nr][nc] == 3:
                    return 1
                elif maze[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append((nr, nc))
    return 0



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                start_r, start_c = r, c 
                break
    print(f'#{tc} {bfs(start_r, start_c)}')
