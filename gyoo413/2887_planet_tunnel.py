import heapq

n = int(input())
planet = [[] for _ in range(n)]
for i in range(n):
    planet[i] = list(map(int, input().split())) + [i]

graph = [[] for _ in range(n)]
for i in range(3):
    planet.sort(key = lambda x:x[i])
    for j in range(n - 1):
        cost = min(abs(planet[j][0] - planet[j + 1][0]),
                   abs(planet[j][1] - planet[j + 1][1]),
                   abs(planet[j][2] - planet[j + 1][2]))
        graph[planet[j][3]].append((cost, planet[j + 1][3]))
        graph[planet[j + 1][3]].append((cost, planet[j][3]))


def prim(start):
    global n
 
    heap = []
    heapq.heappush(heap, (0, start))
    
    MST = [False] * n
    weight = 0
 
    while heap:
        w, node = heapq.heappop(heap)
 
        if MST[node]:
            continue
 
        MST[node] = True
        weight += w
 
        for next_weight, next_node in graph[node]:
            if not MST[next_node]:
                heapq.heappush(heap, (next_weight, next_node))
 
    return weight
 

minimum_weight = prim(0)
print(minimum_weight)