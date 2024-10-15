n = int(input())


def make_star(n):
    star = []

    if n == 3:
        star.append('  *  ')
        star.append(' * * ')
        star.append('*****')
    else:
        t = star(n // 3)
        