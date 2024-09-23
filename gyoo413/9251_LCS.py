string1 = input().strip()
string2 = input().strip()
length1 = len(string1)
length2 = len(string2)

lcs = [[0] * (length2 + 1) for _ in range(length1 + 1)]

for i in range(1, length1 + 1):
    for j in range(1, length2 + 1):
        if string1[i - 1] == string2[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

ans = 0
for i in range(length1 + 1):
    for j in range(length2 + 1):
        if lcs[i][j] > ans:
            ans = lcs[i][j]
print(ans)