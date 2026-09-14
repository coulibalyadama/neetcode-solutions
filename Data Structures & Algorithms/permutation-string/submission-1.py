class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = defaultdict(int)
        for c in s1:
            s1_dict[c] += 1 
        l, r = 0, len(s1)
        while r<=len(s2):
            s2_dict = defaultdict(int)

            for c in s2[l:r]:
                s2_dict[c] += 1 

            if s1_dict == s2_dict:
                return True
            r += 1
            l += 1
        return False
        