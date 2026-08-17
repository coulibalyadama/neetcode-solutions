class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        def count(k):
            res = 0
            while k:
                res += k&1
                k >>= 1
            return res
        for k in range(n+1):
            ans.append(count(k))
        return ans
        