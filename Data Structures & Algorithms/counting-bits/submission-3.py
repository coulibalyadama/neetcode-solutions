class Solution:
    def countBits(self, n: int) -> List[int]:
        # ans = []
        # def count(k):
        #     res = 0
        #     while k:
        #         res += k&1
        #         k >>= 1
        #     return res
        # for k in range(n+1):
        #     ans.append(count(k))
        # return ans

        # ans = []
        # def count(k):
        #     res = 0
        #     while k:
        #         res += k%2
        #         k //= 2
        #     return res
        # for k in range(n+1):
        #     ans.append(count(k))
        # return ans

        # Dynamic Programming
        dp = [0]*(n+1)
        offset = 1
        for i in range(1, n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp
        