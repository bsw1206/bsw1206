from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(start_r, start_c):
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = True # 시작 위치 방문처리
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i] # 4방향 이동
            # 벽 충돌 여부, 방문 여부 파악
            if 0 <= nr < 100 and 0 <= nc < 100 and not visited[nr][nc] and visited[nr][nc] != 1:
                if maze[nr][nc] == 3: # 도착점 발견!
                    return 1
                if maze[nr][nc] == 0: # 길 발견!
                    visited[nr][nc] = True # 방문 처리
                    q.append((nr, nc)) # queue에 경로 추가
    return 0 # 못 찾으면 0 출력

for tc in range(1, 11):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    
    visited = [[0] * 100 for _ in range(100)]
    # start_r, start_c = 1, 1
    result = bfs(1, 1) # 시작 위치 (1,1)로 정했으므로 굳이 따로 정할 필요 x
    print(f'#{T} {result}')
