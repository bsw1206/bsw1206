T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    num_lst = list(map(int, input().split()))
    for i in range(M):
        num_lst.append(num_lst.pop(0))
    print(f'#{tc} {num_lst[0]}')
