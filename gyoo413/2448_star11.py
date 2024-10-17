n = int(input())
n //= 3


def make_star(n):
    star = []

    if n == 1:
        star.append('  *  ')
        star.append(' * * ')
        star.append('*****')
    else:
        t = make_star(n // 2)
        length = len(t)
        for i in range(length):
            star.append(' ' * length + t[i] + ' ' * length)
        for i in range(length):
            star.append(t[i] + ' ' + t[i])

    return star

star = make_star(n)

for arr in star:
    print(*arr, sep='')
