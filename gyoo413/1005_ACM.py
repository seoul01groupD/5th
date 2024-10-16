from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        v1, v2 = map(int, input().split())
        graph[v2].append(v1)
    target = int(input())

    queue = deque()
    visited = [0] * (n + 1)
    visited[target] = time[target]
    queue.append(target)

    while queue:
        now = queue.popleft()
        for next_node in graph[now]:
            if visited[next_node] < visited[now] + time[next_node]:
                visited[next_node] = visited[now] + time[next_node]
                queue.append(next_node)

    print(max(visited))    
    