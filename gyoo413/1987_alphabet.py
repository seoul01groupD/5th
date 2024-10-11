import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(input().strip()) for _ in range(n)]
alphabet = set()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

max_length = 0

def backtracking(now, length):
    global max_length

    x, y = now
    max_length = max(max_length, length)
    
    alphabet.add(matrix[x][y])

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] not in alphabet:
            backtracking((nx, ny), length + 1)

    alphabet.remove(matrix[x][y])


backtracking((0, 0), 1)
print(max_length)