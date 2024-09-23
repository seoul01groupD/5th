string1 = input().strip()
string2 = input().strip()
length1 = len(string1)
length2 = len(string2)

lcs = [[0] * length1 for _ in range(length2)]

