import heapq

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2, w = map(int, input().split())
    graph[v1].append([v2, w])
    
    
def dijkstra(start):
    global n
    
    heap = []
    distance = [float("INF")] * (n + 1)
    heapq.heappush(heap, (start, 0))
    distance[start] = 0
    
    while heap:
        node, cost = heapq.heappop(heap)
        
        if distance[node] < cost:
            continue
        
        for next_node, next_cost in graph[node]:
            new_cost = cost + next_cost
            
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(heap, (next_node, new_cost))

    return distance


dist_list = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist_list[i] = dijkstra(i)
    
ans_list = [0] * (n + 1)
for i in range(1, n + 1):
    ans_list[i] = dist_list[i][x] + dist_list[x][i]

ans = max(ans_list)
print(ans)    