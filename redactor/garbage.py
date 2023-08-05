def de(n):
    cur = 0
    ne = 1
    for _ in range(n):
        yield cur
        cur, ne = ne, ne + cur


def square(x):
    for _ in x:
        yield _ ** 2


fs = de(10)
for i in fs:
    print(i, end=' ')

print(f\n{sum(square(de(5)))}')
