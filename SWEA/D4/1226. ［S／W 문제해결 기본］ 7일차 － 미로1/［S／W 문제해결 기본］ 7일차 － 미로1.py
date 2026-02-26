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
            if 0 <= nr < 16 and 0 <= nc < 16 and not visited[nr][nc] and visited[nr][nc] != 1:
                if maze[nr][nc] == 3:
                    return 1
                if maze[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append((nr, nc))
    return 0







for tc in range(1, 11):
    T = int(input())
    maze = [list(map(int, list(input()))) for _ in range(16)]
    
    visited = [[False] * 16 for _ in range(16)]
    # start_r, start_c = 1, 1
    result = bfs(1, 1)
    print(f'#{T} {result}')
