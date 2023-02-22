#!/bin/python3
'''
It's really easy to have off-by-1 errors in these problems.
Pay very close attention to your list indexes and your < vs <= operators.
'''

def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.
    '''
    def find_smallest_positive_helper(xs, low, high):
        if low > high:
            return None

        mid = (low + high) // 2

        if xs[mid] > 0:
            if mid == 0 or xs[mid - 1] <= 0:
                return mid
            else:
                return find_smallest_positive_helper(xs, low, mid - 1)
        else:
            return find_smallest_positive_helper(xs, mid + 1, high)

    return find_smallest_positive_helper(xs, 0, len(xs) - 1)


def count_repeats(xs, x):
    """
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.
    """
    def leftmost(xs, x, lo, hi):
        while lo <= hi:
            mid = (lo + hi) // 2
            if xs[mid] == x:
                if mid == 0 or xs[mid - 1] != x:
                    return mid
                hi = mid - 1
            elif xs[mid] < x:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

    def rightmost(xs, x, lo, hi):
        while lo <= hi:
            mid = (lo + hi) // 2
            if xs[mid] == x:
                if mid == len(xs) - 1 or xs[mid + 1] != x:
                    return mid
                lo = mid + 1
            elif xs[mid] < x:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1
    left = leftmost(xs, x, 0, len(xs) - 1)
    if left == -1:
        return 0
    right = rightmost(xs, x, left, len(xs) - 1)
    return right - left + 1


def count(xs, x):
    """
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.
    """
    def leftmost(xs, x, lo, hi):
        while lo <= hi:
            mid = (lo + hi) // 2
            if xs[mid] == x:
                if mid == 0 or xs[mid - 1] != x:
                    return mid
                hi = mid - 1
            elif xs[mid] < x:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

    def rightmost(xs, x, lo, hi):
        while lo <= hi:
            mid = (lo + hi) // 2
            if xs[mid] == x:
                if mid == len(xs) - 1 or xs[mid + 1] != x:
                    return mid
                lo = mid + 1
            elif xs[mid] < x:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1
    left = leftmost(xs, x, 0, len(xs) - 1)
    if left == -1:
        return 0
    right = rightmost(xs, x, left, len(xs) - 1)
    return right - left + 1


def argmin(f, lo, hi, epsilon=1e-3):
    if hi - lo < epsilon:
        return (lo + hi) / 2

    m1 = lo + (hi - lo) / 3
    m2 = hi - (hi - lo) / 3

    if f(m1) < f(m2):
        return argmin(f, lo, m2, epsilon)
    else:
        return argmin(f, m1, hi, epsilon)


def find_boundaries(f):
    lo = -1
    hi = 1

    while f(hi) < f(lo):
        lo = hi
        hi *= 2

    while hi - lo > 1e-6:
        mid = (lo + hi) / 2
        if f(mid) < f(mid + 1e-6):
            hi = mid
        else:
            lo = mid

    return lo, hi


def argmin_simple(f, epsilon=1e-3):
    lo, hi = find_boundaries(f)
    return argmin(f, lo, hi, epsilon)
