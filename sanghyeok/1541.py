arr = input()

parts = arr.split('-')

before_part_sum = sum(map(int, parts[0].split('+')))

result = before_part_sum
for part in parts[1:]:
    part_sum = sum(map(int, part.split('+')))
    result -= part_sum

print(result)

