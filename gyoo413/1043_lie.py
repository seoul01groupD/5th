n, m = map(int, input().split())
truth_dict = {x : False for x in range(1, n + 1)}
truth_list = list(map(int, input().split()))[1:]
for x in truth_list:
    truth_dict[x] = True

parties = [[] for _ in range(m)]
for i in range(m):
    temp = list(map(int, input().split()))[1:]
    parties[i] = temp

for _ in range(m):
    for party in parties:
        for people in party:
            if truth_dict[people]:
                for x in party:
                    truth_dict[x] = True
                break

cnt = 0
for party in parties:
    for people in party:
        if truth_dict[people]:
            break
    else:
        cnt += 1

print(cnt)