class Solution:
    def reverseBits(self, n: int) -> int:
        count = 31
        res = 0
        while n:
            if n%2 == 0:
                res *= 2
            else:
                res = res * 2 + 2
            n //= 2
            count -= 1
        return int(res * 2**count)
        