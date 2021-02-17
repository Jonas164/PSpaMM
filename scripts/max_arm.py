def getBlocksize(m, n, bk):
    bm = 2
    bn = 1
    maxval = 0

    for i in range(2, m + 1, 2):
        for j in range(1, n + 1):
            if ARM_condition(i, j, bk):
                if i * j > maxval:
                    maxval = i * j
                    bm = i
                    bn = j

    return (bm, bn)


def ARM_condition(bm, bn, bk):
    return (bn + bk) * (bm / 2) + bn + 2 <= 32
