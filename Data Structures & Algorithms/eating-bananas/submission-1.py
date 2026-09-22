class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # min_h = float("inf")
        # k = 0
        # while min_h > h:
        #     k += 1
        #     min_h = 0
        #     for i in piles:
        #         min_h += math.ceil(i/k)

        # return k

        l = 1
        r = max(piles)
        res = max(piles)

        while l <= r:
            m = (l+r)//2
            temp = 0
            for p in piles:
                temp += math.ceil(p/m)
            if temp <= h:
                res = min(m, res)
                r = m-1
            else:
                l = m+1
        return res



