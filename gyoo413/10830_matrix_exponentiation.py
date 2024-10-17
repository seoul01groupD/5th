from copy import deepcopy

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def exponent(n):
    powers = []
    power = 0

    while n > 0:
        if n % 2 == 1:
            powers.append(1)
        else:
            powers.append(0)
        n //= 2
        power += 1

    return powers


def matrix_time(mat1, mat2):
    l = len(mat1)
    result = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            for k in range(l):
                result[i][j] += mat1[i][k] * mat2[k][j]
                result[i][j] %= 1000

    return result


binary = exponent(b)

ans = [[0] * n for _ in range(n)]
for i in range(n):
    ans[i][i] = 1

for idx, coef in enumerate(binary):
    if idx == 0:
        matrix = matrix
    else:
        matrix = matrix_time(matrix, matrix)
    if coef == 1:
        ans = matrix_time(ans, matrix)
    

for i in range(n):
    print(*ans[i])
