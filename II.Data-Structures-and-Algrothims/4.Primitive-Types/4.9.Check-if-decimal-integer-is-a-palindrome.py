# O(n) - time complexity
# O(1) - space complexity

import math

def is_palindrome(x):
    if x <= 0:
        return x == 0

    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10**(num_digits - 1)
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask # Remove the most significant digit of x.
        x //= 10 # Remove the least significant digit of x.
        msd_mask //= 100
    return True