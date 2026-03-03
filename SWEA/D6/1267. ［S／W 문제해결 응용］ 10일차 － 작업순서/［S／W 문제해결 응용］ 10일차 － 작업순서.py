
def dfs(i):
    visited[i] = True
    for neighbor in tree[i]:
        if not visited[neighbor]:
            dfs(neighbor)

    result.append(i)


for tc in range(1, 11):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    visited = [False] * (V + 1)

    tree = [[] for _ in range(V + 1)]
    for i in range(E):
        p, c = data[i*2], data[i*2+1]
        tree[p].append(c)

    result = []
    for i in range(1, V + 1):
        if not visited[i]:
            dfs(i)
    print(f'#{tc}', *result[::-1])    
    