import heapq

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    order = [[] for _ in range(n + 1)]
    for _ in range(k):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        order[v2].append(v1)
    target = int(input())
    start = []
    for i in range(1, len(order)):
        if not order[i]:
            start.append((0, i))

    
    def bfs():
        global n, target

        heap = heapq.heapify(start)
        visited = [0] * (n + 1)
        parent = [[0] for _ in range(n + 1)]
        for cost, node in start:
            visited[node] = 1

        duration = 0
        
        while heap:
            now = heapq.heappop(heap)
            for next_node in graph[now]:
                if visited[next_node] < len(order[next_node]) - 1:
                    visited[next_node] += 1
                    parent[next_node].append(time[now])
                elif visited[next_node] == len(order[next_node]) - 1:
                    visited[next_node] += 1
                    parent[next_node].append(time[now])
                    heapq.heappush(heap, (max(parent[next_node]), next_node))
                    
                    
    print(bfs())

