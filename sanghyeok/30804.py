N = int(input())
S = list(map(int, input().split()))


left = 0
right = 0
max_length = 0
count =[0]*10

while right <N:
    count[S[right]] +=1

    while True:
        num = 0
        for i in count:
            if i > 0:
                num +=1

        if num <=2:
            break

        count[S[left]] -=1
        left +=1

    current_length = right - left + 1
    max_length = max(current_length,max_length)

    right +=1

result = max_length
print(result)