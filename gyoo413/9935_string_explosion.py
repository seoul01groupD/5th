string = input().strip()
n = len(string)
bomb = input().strip()
k = len(bomb)

stack = []
for i in range(n):
    stack.append(string[i])
    if string[i] == bomb[-1]:
        if len(stack) < k:
            continue
        for j in range(k):
            if stack[-1 - j] != bomb[-1 - j]:
                break
        else:
            for _ in range(k):
                stack.pop()
                
if stack:
    print(''.join(stack))
else:
    print("FRULA")