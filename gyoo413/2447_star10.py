n = int(input())


def make_star(n):
    star = []

    if n == 3:
        star.append('***')
        star.append('* *')
        star.append('***')
    else:
        t = make_star(n // 3)
        for i in range(len(t)):
            star.append(t[i] * 3)
        for i in range(len(t)):
            star.append(t[i] + ' ' * len(t) + t[i])
        for i in range(len(t)):
            star.append(t[i] * 3)
        # for i in range(len(t)):
        #     print(t[i] * 3, end='')
        #     print()
        # for i in range(len(t)):
        #     print(t[i], ' ' * len(t), t[i], sep='', end='')
        #     print()
        # for i in range(len(t)):
        #     print(t[i] * 3, end='')
        #     print()
        
    return star

# make_star(n)
star = make_star(n)
for i in range(len(star)):
    print(*star[i], sep='')
