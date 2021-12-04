def point_2():
    k = 0
    for first in range(2, 23, 2):
        for second in range(2, 23, 2):
            s = first + second
            if s < 19:
                k += 1
    return k/11**2

def point_3():
    k = 0
    for first in range(2, 23, 2):
        for second in range(2, 23, 2):
            for third in range(2, 23, 2):
                s = first + second + third
                if s > 56:
                    k += 1
    return k/11**3

def point_5():
    k = 0
    vsego = 0
    for ff in range(2, 23, 2):
        for sf in range(2, 23, 2):
            for fs in range(2, 23, 2):
                for ss in range(2, 23, 2):
                    pair_1 = ff + sf
                    pair_2 = fs + ss
                    vsego += 1
                    if pair_1 == pair_2:
                        k += 1
    return k/vsego

print(point_2(), point_3(), point_5())




