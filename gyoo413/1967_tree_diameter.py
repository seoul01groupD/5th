from collections import deque

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    v1, v2, w = map(int, input().split())
    tree[v1].append([v2, w])
    tree[v2].append([v1, w])


def bfs(start):
    queue = deque()
    visited = [-1] * (n + 1)
    queue.append(start)
    visited[start] = 0
    max_weight = 0
    max_weight_node = start

    while queue:
        now = queue.popleft()
        for next, weight in tree[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + weight
                queue.append(next)
                if visited[next] > max_weight:
                    max_weight = visited[next]
                    max_weight_node = next

    return max_weight_node, max_weight


max_weight_node, _ = bfs(1)
_, max_weight = bfs(max_weight_node)
print(max_weight)