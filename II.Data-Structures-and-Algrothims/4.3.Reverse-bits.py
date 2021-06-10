# O(n/L) 
# n-bit integer
# L-bit cache keys 
 
def reverse_bits(x):
    PRECOMPUTED_REVERSE = ['00', '10', '01', '11']
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED_REVERSE[x & BIT_MASK] << (3 * MASK_SIZE)
            | PRECOMPUTED_REVERSE[(x >> MASK_SIZE) & BIT_MASK] <<
            (2 * MASK_SIZE) | 
            PRECOMPUTED_REVERSE[(x >> (2 * MASK_SIZE)) & BIT_MASK] << MASK_SIZE
            | PRECOMPUTED_REVERSE[(x >> (3 * MASK_SIZE)) & BIT_MASK])