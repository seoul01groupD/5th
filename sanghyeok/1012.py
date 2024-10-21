from collections import deque

def bfs(start_row, start_col):
    queue = deque()
    queue.append((start_row,start_col))
    visited[start_row][start_col] = 1

    while queue:
        row, col = queue.popleft()
        for k in range(4):
            n_row = row + d_row[k]
            n_col = col + d_col[k]
            if 0<=n_row<M and 0<=n_col<N and visited[n_row][n_col] == 0 and arr2[n_row][n_col] == 1:
                visited[n_row][n_col] = 1
                queue.append((n_row,n_col))


T = int(input())

for tc in range(T):
    M, N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(K)]
    arr2 = [[0]*N for _ in range(M)]
    for a,b in arr:
        arr2[a][b] = 1

    d_row = [1,0,0,-1]
    d_col = [0,1,-1,0]
    count = 0
    visited = [[0] * N for _ in range(M)]
    for row in range(M):
        for col in range(N):
            if arr2[row][col] == 1 and visited[row][col] == 0:
                bfs(row,col)
                count +=1

    print(count)



