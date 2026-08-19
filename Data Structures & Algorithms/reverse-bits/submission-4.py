class Solution:
    def reverseBits(self, n: int) -> int:
        # count = 31
        # res = 0
        # while n:
        #     if n&1 == 0:
        #         res *= 2
        #     else:
        #         res = res * 2 + 2
        #     n >>= 1
        #     count -= 1
        # return int(res * 2**count)

        res = 0
        for i in range(32):
            bit = (n >> i)&1
            res = (res << 1) | bit
        return res