r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def diffusion():
    temp_room = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                diffused = room[i][j] // 5
                count = 0
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < r and 0 <= y < c and room[x][y] != -1:
                        temp_room[x][y] += diffused
                        count += 1
                temp_room[i][j] += room[i][j] - diffused * count
            else:
                temp_room[i][j] += room[i][j]
    return temp_room


for i in range(r):
    if room[i][0] == -1:
        cleaner1 = i
        break
cleaner2 = cleaner1 + 1

def circulate1(cleaner):
    for i in range(cleaner - 2, -1, -1):
        room[i + 1][0] = room[i][0]
    for j in range(1, c):
        room[0][j - 1] = room[0][j]
    for i in range(1, cleaner + 1):
        room[i - 1][c - 1] = room[i][c - 1]
    for j in range(c - 2, 0, -1):
        room[cleaner][j + 1] = room[cleaner][j]
    room[cleaner][1] = 0

def circulate2(cleaner):
    for i in range(cleaner + 2, r):
        room[i - 1][0] = room[i][0]
    for j in range(1, c):
        room[r - 1][j - 1] = room[r - 1][j]
    for i in range(r - 2, cleaner + 1, -1):
        room[i + 1][c - 1] = room[i][c - 1]
    for j in range(c - 2, 0, -1):
        room[cleaner][j + 1] = room[cleaner][j]
    room[cleaner][1] = 0

for _ in range(t):
    room = diffusion()
    circulate1(cleaner1)
    circulate2(cleaner2)

finedust = 0
for row in room:
    finedust += sum(row)

print(finedust + 2)
