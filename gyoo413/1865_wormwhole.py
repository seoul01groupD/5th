tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        v1, v2, c = map(int, input().split())
        graph[v1].append((v2, c))
        graph[v2].append((v1, c))
    for _ in range(w):
        v1, v2, c = map(int, input().split())
        graph[v1].append((v2, -c))


    def bellman_ford(start):
        global n

        distance = [float('inf') for _ in range(n + 1)]
        distance[start] = 0

        for _ in range(n - 1):
            for u in range(1, n + 1):
                for v, w in graph[u]:
                    if distance[u] != float('inf') and distance[u] + w < distance[v]:
                        distance[v] = distance[u] + w

        for u in range(1, n + 1):
            for v, w in graph[u]:
                if distance[u] != float('inf') and distance[u] + w < distance[v]:
                    return True

        return False
    
    cycle = [0] * (n + 1)

    def dfs(start):
        stack = []
        visited = [0] * (n + 1)
        visited[start] = 1
        cycle[start] = 1
        now = start
        

        while True:
            for next, w in graph[now]:
                if visited[next] == 0:
                    visited[next] = 1
                    stack.append(now)
                    cycle[now] = 1
                    now = next
                    break
            else:
                if stack:
                    now = stack.pop()
                else:
                    return

    for v in range(1, n + 1):
        if cycle[v] == 0:
            dfs(v)
            if bellman_ford(v):
                print("YES")
                break
    else:
        print("NO")
