#!/usr/bin/env python3
# Author Dario Clavijo 2021
# run with: python3 -m flamegraph -o perf.log powtest.py ; code/FlameGraph/flamegraph.pl --title "Pow perf" perf.log > perf.svg

from gmpy2 import isqrt, powmod
import time
import sys


def _pow2mod_bitshift(b, m):
    return (1 << b) % m


def _powmod_bs(x, y, z):
    "Bruce Schneier's powmod "
    number = 1
    while y:
        if y & 1:
            number = (number * x) % z
        y >>= 1
        x = (x * x) % z
    return number


def _powmod_catch2(a, b, m, F=pow):
    return (1 << b) % m if a == 2 else F(a, b, m)

def _powmod_catch22(a, b, m):
    #if a == 2:
    #if 1:
        return powmod(a, b, m)
    #else:
    #    return powmod(a, b, m)


def _powmod_catchEven(a, b, m, F=pow):
    if 1 >= a >= 0 and b >= 0:
        return 1
    if a == 2:
        return (1 << b) % m
    return (((1 << b) % m) * F(a >> 1, b, m)) % m if a & 1 == 0 else F(a, b, m)


def _pow(a, b, m=None, F=powmod, verbose=False):
    if verbose:
        print("pow", a, b, m)

    def __powmod(a, b, m, F=F):
        return F(a, b, m) if m != None else pow(a, b)

    if 1 >= a >= 0:
        r = 1
    elif b == 0:
        r = 1
    elif a == 2:
        #if m != None:
        r = (1 << b) % m
        #else:
        #    r = (1 << b)
    elif b == 2:
        r = a * a
    elif a == m:
        r = 0
    elif m == 2:
        r = a & 1
    elif a & 1 == 0:
        #if m != None:
        r = ((1 << b) % m) * _pow(a >> 1, b, m)
        #else:
        #    r = (1 << b) * _pow(a >> 1, b, m)
    elif a & 1 == 1:
        if a > 4:
            i = isqrt(a)
            if (i * i) == a and i > 1:
                x = _pow(i, b, m) if b > 2 else a
                r = _pow(x, 2, m)
            else:
                r = None
                for p in [3, 5, 7, 11]:
                    if a % p == 0:
                        r = __powmod(p, b, m) * _pow(a // p, b, m)
                if r is None:
                    r = __powmod(a, b, m)
        elif a == 3:
            r = __powmod(a, b, m) if b > 2 else 3 << b
    else:
        return __powmod(a, b, m)
    # print(r)
    if m != None:
        r = r % m
    return r


_powmod_complex = _pow


def test0():
    print("test")
    l = 10
    ok = True
    for i in range(0, l):
        for j in range(0, l):
            for m in range(1, l):
                # print(i,j,m)
                x = pow(i, j, m)
                y = _pow(i, j, m)
                ok = x == y
                # print(i,j,x,y,ok)
                if not ok:
                    print("nok", i, j, m)
                    sys.exit(1)


def test2():
    a = 2 * 5 * 3 * 3 * 7 * 11 * 17
    # a = 17*2
    # print(_pow(1,3))
    # print(_pow(3,3))
    print(_pow(a, 3, 65537 ** 2, F=pow))
    print(pow(a, 3, 65537 ** 2))


def _pow2mod_f(b, m, F=pow):
    return F(2, b, m)


def timeit(f, l, F=None):
    t0 = time.time()
    for a in range(0, l):
        for b in range(0, l):
            for m in range(1, l):
                if F is None:
                    f(a, b, m)
                else:
                    # f(a,b,m, F=F, verbose=False)
                    f(a, b, m, F=F)
    Fn = F.__name__ if F != None else "None"
    print("%s %s %f" % (f.__name__.ljust(30), Fn.ljust(30), time.time() - t0))


def timeit2(f, l, F=None):
    t0 = time.time()
    for b in range(0, l):
        for m in range(1, l):
            if F is None:
                f(b, m)
            else:
                f(b, m, F=F)
    Fn = F.__name__ if F != None else "None"
    print("%s %s %f" % (f.__name__.ljust(30), Fn.ljust(30), time.time() - t0))


def test3(l):
    print("=" * 80)
    print("Iterations: %d" % l)
    print("Func Name: ".ljust(30) + " Native Func: ".ljust(30) + " Time:")
    print("=" * 80)

    timeit2(_pow2mod_bitshift, l, None)
    timeit2(_pow2mod_f, l, pow)
    timeit2(_pow2mod_f, l, powmod)


def test4(l):
    print("=" * 80)
    print("Iterations: %d" % l)
    print("Func Name: ".ljust(30) + " Native Func: ".ljust(30) + " Time:")
    print("=" * 80)

    timeit(pow, l, None)
    timeit(powmod, l, None)
    timeit(_powmod_bs, l, None)

    print("-" * 80)

    timeit(_powmod_catch2, l, pow)
    timeit(_powmod_catch2, l, powmod)
    timeit(_powmod_catch22, l)
    timeit(_powmod_catch2, l, _powmod_bs)

    print("-" * 80)

    timeit(_powmod_catchEven, l, pow)
    timeit(_powmod_catchEven, l, powmod)
    timeit(_powmod_catchEven, l, _powmod_bs)

    print("-" * 80)

    timeit(_powmod_complex, l, pow)
    timeit(_powmod_complex, l, powmod)
    timeit(_powmod_complex, l, _powmod_bs)


if __name__ == "__main__":
    test3(1200)
    test4(100)


