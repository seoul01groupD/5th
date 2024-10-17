def dfs(temp = []):
    if len(temp) == m:
        for i in temp:
            print(nums[i], end=' ')

        return print()

    start = 0

    if temp:
        start = temp[-1]

    for i in range(start, l):
        temp.append(i)
        dfs(temp)
        temp.pop()

n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
l = len(nums)
dfs()