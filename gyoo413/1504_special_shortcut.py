import heapq

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))
middle1, middle2 = map(int, input().split())

def dijkstra(start, target):
    heap = []
    distance = [float('inf')] * (v + 1)
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        cost, node = heapq.heappop(heap)

        if distance[node] < cost:
            continue

        for next_node, next_cost in graph[node]:
            new_cost = distance[node] + next_cost

            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return distance[target]

dist1 = dijkstra(1, middle1) + dijkstra(middle1, middle2) + dijkstra(middle2, v)
dist2 = dijkstra(1, middle2) + dijkstra(middle2, middle1) + dijkstra(middle1, v)

ans = min(dist1, dist2)
if ans == float('inf'):
    print(-1)
else:
    print(ans)