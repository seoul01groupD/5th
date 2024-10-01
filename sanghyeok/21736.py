from collections import deque

def bfs(row,col):
    global cnt
    queue.append((row,col))
    visited[row][col] = 1

    while queue:
        n_row,n_col= queue.popleft()
        for k in range(4):
            k_row = n_row + d_row[k]
            k_col = n_col + d_col[k]
            if 0 <= k_row < N and 0 <= k_col < M and visited[k_row][k_col] == 0:
                if arr[k_row][k_col] == 'P':
                    queue.append((k_row,k_col))
                    cnt += 1
                    visited[k_row][k_col] = 1
                elif arr[k_row][k_col] == 'O':
                    queue.append((k_row, k_col))
                    visited[k_row][k_col] = 1
                elif arr[k_row][k_col] == 'X':
                    visited[k_row][k_col] = 1







N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]


d_row = [0,0,1,-1]
d_col = [1,-1,0,0]
cnt = 0
queue = deque()
visited = [[0]*M for _ in range(N)]
for row in range(N):
    for col in range(M):
        if arr[row][col] == 'I':
            bfs(row,col)

if cnt !=0:
    print(cnt)
else:
    print('TT')






