from collections import deque
import sys
input = sys.stdin.readline
def D(n):
    n = n*2
    if n > 9999:
        n = n%10000
    return n
def S(n):
    n = n-1
    if n == -1:
        n = 9999
    return n

def L(n):
    return (n % 1000) * 10 + (n // 1000)


def R(n):
    return (n % 10) * 1000 + (n // 10)


def bfs(start, target):
    queue = deque([(start, "")])
    visited = [0]*10001
    visited[start] = 1

    while queue:
        i, path = queue.popleft()

        if i == target:
            return path

        for a,b in [("D", D),("S",S),('L',L),('R',R)]:
            next_value = b(i)
            if visited[next_value] == 0:
                visited[next_value] = 1
                queue.append((next_value,path+a))
T = int(input())

for tc in range(1, T+1):
    A, B = map(int,input().split())
    result = bfs(A,B)
    print(result)