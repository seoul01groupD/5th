import sys
sys.setrecursionlimit(10**6)

lst = []
while True:
    try:
        lst.append(int(input().strip()))
    except:
        break
n = len(lst)

tree = [[] for _ in range(n)]

def find_postorder(preorder, start, end):
    if start > end:
        return []

    right_node = start + 1
    while right_node <= end and preorder[right_node] < preorder[start]:
        right_node += 1

    left_postorder = find_postorder(preorder, start + 1, right_node - 1)
    right_postorder = find_postorder(preorder, right_node, end)

    return left_postorder + right_postorder + [preorder[start]]

postorder = find_postorder(lst, 0, n - 1)
for v in postorder:
    print(v)