from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
tree = [[] for _ in range(v + 1)]
for _ in range(1, v + 1):
    temp = list(map(int, input().split()))
    v1 = temp[0]
    for i in range(1, len(temp) - 1, 2):
        v2, w = temp[i], temp[i + 1]
        tree[v1].append((v2, w))


def bfs(start):
    queue = deque()
    visited = [-1] * (v + 1)
    queue.append(start)
    visited[start] = 0
    max_weight_node = start
    max_weight = 0

    while queue:
        now = queue.popleft()
        for next, weight in tree[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + weight
                queue.append(next)
                if max_weight < visited[next]:
                    max_weight = visited[next]
                    max_weight_node = next

    return max_weight, max_weight_node


_, max_weight_node = bfs(1)
max_weight, _ = bfs(max_weight_node)
print(max_weight)