class Solution:
    def longestPalindrome(self, s: str) -> str:
        # # Brute Force
        # def is_palindrome(s):
        #     l, r = 0, len(s) - 1
        #     while l < r:
        #         if s[l] != s[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True

        # res = s[0]
        # length = 1
        # for k in range(len(s)):
        #     for j in range(k+1, len(s)):
        #         if j - k + 1 > length and is_palindrome(s[k:j+1]):
        #             res = s[k:j+1]
        #             length = j - k + 1
        # return res

        length = 0
        res = s[0]
        for k in range(len(s)):
            r, l = k, k
            while l>=0 and r<len(s) and s[r]==s[l]:
                r += 1
                l -= 1
            if r-l-1 > length:
                res = s[l+1:r]
                length = r-l-1
            
            # r, l = k, k - 1
            # while l>=0 and r<len(s) and s[r]==s[l]:
            #     r += 1
            #     l -= 1
            # if r-l-1 > length:
            #     res = s[l+1:r]
            #     length = r-l-1
            
            r, l = k + 1, k
            while l>=0 and r<len(s) and s[r]==s[l]:
                r += 1
                l -= 1
            if r-l-1 > length:
                res = s[l+1:r]
                length = r-l-1
            
        return res
        