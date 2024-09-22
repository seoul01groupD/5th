import sys
input = sys.stdin.readline

lst = []
while True:
    try:
        lst.append(int(input().strip()))
    except:
        break

