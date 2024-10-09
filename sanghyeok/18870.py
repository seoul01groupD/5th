N = int(input())

arr = list(map(int, input().split()))
sorted_arr = sorted(set(arr))

index_dic = {}

for idx, value in enumerate(sorted_arr):
    if value not in index_dic:
        index_dic[value] = idx
    else:
        pass




result = []
for i in arr:
    result.append(index_dic[i])
# print(index_dic)
print(*result)

