n = int(input())
dp_max = [0] * 3; dp_min = [0] * 3

for _ in range(n):
    lst = list(map(int, input().split()))

    temp_max = dp_max.copy()
    dp_max[0] = max(temp_max[0], temp_max[1]) + lst[0]
    dp_max[1] = max(temp_max[0], temp_max[1], temp_max[2]) + lst[1]
    dp_max[2] = max(temp_max[1], temp_max[2]) + lst[2]

    temp_min = dp_min.copy()
    dp_min[0] = min(temp_min[0], temp_min[1]) + lst[0]
    dp_min[1] = min(temp_min[0], temp_min[1], temp_min[2]) + lst[1]
    dp_min[2] = min(temp_min[1], temp_min[2]) + lst[2]

print(max(dp_max))
print(min(dp_min))