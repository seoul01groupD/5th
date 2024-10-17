import heapq

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(r):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance = [float('inf')] * (n + 1)
    distance[start] = 0

    while heap:
        cost, now = heapq.heappop(heap)
        if distance[now] < cost:
            continue

        for next_node, next_cost in graph[now]:
            new_cost = distance[now] + next_cost
            if distance[next_node] > new_cost:
                distance[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return distance


max_item = 0
for node in range(1, n + 1):
    distance = dijkstra(node)
    temp_item = 0
    for i in range(1, n + 1):
        if distance[i] <= m:
            temp_item += items[i]
    if temp_item > max_item:
        max_item = temp_item

print(max_item)