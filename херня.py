from functools import partial


def f(x, q):
    _, (e, _), y = x
    m = e + y
    print(m)
    z = m * q
    print(z)


fn2 = partial(f, [4, [7, 8], 6])

print(fn2(2))


def m(r):
    m = 0
    for (_, (x, _)) in r:
        m = m + x
    print(m)


print(m([(3, [9, 1]), [(23, 43), [5, 4]]]))

import time
from datetime import datetime


def plus5(z):
    print('Nomer ' + str(z))
    time.sleep(1)
    return z + 5


def lazy_map(fn, ls):
    for x in ls:
        y = fn(x)
        yield y


start = datetime.now()
gen = lazy_map(plus5, range(1000000))
print(next(gen))
print(next(gen))
print("prog time" + str((datetime.now() - start).total_seconds()) + ' sec')
