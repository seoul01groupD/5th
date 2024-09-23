n = int(input())
seq1 = list(map(int, input().split()))
m = int(input())
seq2 = list(map(int, input().split()))


def find_max(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] > arr2[j]:
                break
            elif arr1[i] == arr2[j]:
                return arr1[i]
            
    return False

k = 0
sub_seq = []

while True:
    sorted_seq1 = sorted(seq1, reverse=True)
    sorted_seq2 = sorted(seq2, reverse=True)            

    if find_max(sorted_seq1, sorted_seq2):
        M = find_max(sorted_seq1, sorted_seq2)
        k += 1
        sub_seq.append(M)
        idx1 = seq1.index(M)
        idx2 = seq2.index(M)
        seq1 = seq1[idx1 + 1:]
        seq2 = seq2[idx2 + 1:]
    else:
        break

print(k)
print(*sub_seq)