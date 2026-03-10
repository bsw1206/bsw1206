T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    n_lst = list(map(int, input().split()))
    m_lst = list(map(int, input().split()))
    
    n_lst.sort(reverse = True)
    m_lst.sort(reverse = True)
    sum_val = 0
    
    for i in m_lst:
        for j in range(len(n_lst)):
            if i >= n_lst[j]:
                sum_val += n_lst.pop(j)
                break
    
    print(f'#{tc} {sum_val}')