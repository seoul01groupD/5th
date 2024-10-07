n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    v1, v2, w = map(int, input().split())
    tree[v1].append([v2, w])
    tree[v2].append([v1, w])


def dfs(start, end):
    stack = []
    stack.append(start)
    visited = [0] * (n + 1)
    visited[start] = 1

    while True:
        for next, weight in tree[start]:
            