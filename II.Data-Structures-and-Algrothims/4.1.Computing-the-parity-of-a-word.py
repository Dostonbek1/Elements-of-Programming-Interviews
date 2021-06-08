# The parity of a binary word is 1 if the number of 1s in the word is odd;
# otherwise, it is 0. For example, the parity of 1011 is 1, and the partiy of 10001000
# is 0. Parity checks are used to detect single bit errors in data storage and communication.

# O(n)
def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

# O(k)
def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1 # Drops the lowest set bit of x.
    return result

# O(n/L)
def parity(x):
    MASK_SIZE = 6
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED_PARITY[X >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^
            PRECOMPUTED_PARITY[x & BIT_MASK])

# O(logn)
def parity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1