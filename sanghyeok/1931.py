
N = int(input())
arr = []
for tc in range(N):
    arr2 = list(map(int, input().split()))
    arr.append(arr2)

arr.sort(key=lambda x:(x[1],x[0]))
cnt = 0
finish = 0

for start, end in arr:
    if start >= finish:
        cnt +=1
        finish = end
print(cnt)


